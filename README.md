 Step 1: 
BEGIN

  dbms_cloud.copy_data(
    schema_name => '$[statement.getStagingSchema()]',
{# IF ($[dynamicURIList] != 'true') #}
    table_name =>'$[statement.getStagingTableName()]',
    file_uri_list =>'{# FOR ($[statement.getResourceList()]) IN ($[RESOURCE]) SEP = ',' #}$[statement.getDirectory()]/o/$[RESOURCE]{# ENDFOR #}',
{# ELSE #}
    table_name => staging_table_name,
    file_uri_list => uri_list,
{# ENDIF #}
    credential_name =>'$[statement.getCredentialName()]',
{# IF ($[statement.getFieldsDefinitions()] != '') #}
    field_list => '$[statement.getFieldsDefinitions()]',
{# ENDIF #}
    format => json_object(
{# IF ($[statement.getFileFormat()]  == 'F') #}
    'delimiter' VALUE '',
    'recorddelimiter' VALUE '$[statement.getRecordSeparator()]',
  {# IF ($[statement.getTextDelimiter()]  != '') #}
    'quote' VALUE '$[statement.getTextDelimiter()]',
  {# ENDIF #}
{# ELSIF ($[statement.getFileFormat()]  == 'D') #}
    'delimiter' VALUE '$[statement.getFieldSeparator()]',
    'recorddelimiter' VALUE '$[statement.getRecordSeparator()]',
  {# IF ($[statement.getTextDelimiter()]  != '') #}
    'quote' VALUE '$[statement.getTextDelimiter()]',
  {# ENDIF #}
{# ELSIF ($[statement.getFileFormat()]  == 'CSV') #}
    'type' VALUE '$[statement.getFileFormat()]',
{# ENDIF #}
    'skipheaders' VALUE '$[statement.getSkipHeaders()]'{# IF (!$[statement.getFormatProperties().isEmpty()]) #},
    {# FOR ($[statement.getFormatProperties()]) IN ($[PROP]) SEP = ',
    ' #}$[PROP]{# ENDFOR #}{# ENDIF #}{# IF ($[statement.getFormatPropertiesPlus()] != '') #},
    $[statement.getFormatPropertiesPlus()]{# ENDIF #})
 );
  
END;
            
            

{#NL#}
SELECT {# IF ($[QUERY.hasSelectHints()] == 'true') #}
  /*+ {# FOR ($[QUERY.getSelectHints()]) IN ($[HL]) SEP = '  ' #} $[HL] {# ENDFOR #} */ {# ENDIF #}
{# IF $[QUERY.isDistinct()] #}{#NL#}
  DISTINCT 
{# ENDIF #}
{# IF ($[QUERY.getAliasList()] != 'null') #}{#NL#}
{# LIST #}  $[QUERY.getSelectList().foreach(getText())] $[QUERY.getColumnAliasSeparator()] $[QUERY.getAliasList()] {# SEP #},{#NL#}{# ENDLIST #} 
{# ELSE #}{#NL#}
{# LIST #}  $[QUERY.getSelectList().foreach(getText())] {# SEP #},{#NL#}{# ENDLIST #}
{# ENDIF #} 
{#NL#}
{# IF $[QUERY.isConstantQuery()] #} 
{#NL#}
$[QUERY.getConstantFromClauseText()] 
{# ELSE #}FROM {#NL#}
{# LIST #}  $[QUERY.getFromList().foreach(getText())]{# SEP #} ,{#NL#} {# ENDLIST #} 
{# ENDIF #} 
{# IF ($[QUERY.isPivot()] == 'true') #}
  PIVOT {# IF ($[QUERY.isGenerateXML()] == 'true') #} XML  {# ENDIF #}
  (
    {# FOR ($[QUERY.getAggregateExpressions()]) IN ($[AE]) SEP = ',  ' #} $[QUERY.getAggregateFunction()]($[AE]) AS $[AE] {# ENDFOR #}
    for $[QUERY.getRowLocatorExpressionAlias()] in
    ({# IF ($[QUERY.isGenerateXML()] == 'true') #}{# IF ($[QUERY.getSubQuerytoGenerateXML()] != 'null' AND $[QUERY.getSubQuerytoGenerateXML().length()] > '0') #}
             $[QUERY.getSubQuerytoGenerateXML()] {# ELSE #}
             ANY{# ENDIF #}{# ELSE #}
             {# FOR ($[QUERY.getInColumnMatchingRows()],$[QUERY.getInColumnAliases()]) IN ($[SL],$[AL]) SEP = ',  ' #} $[SL]  AS $[AL] {# ENDFOR #}{# ENDIF #}
    )
  ){# ENDIF #}
{# IF ($[QUERY.getWhereList()] != 'null' AND $[QUERY.getWhereList().size()] > '0') #}{#NL#}
WHERE{#NL#}
{# LIST #}  ($[QUERY.getWhereList()]{#NL#}) {# SEP #}AND {# ENDLIST #}
{# ENDIF #}
{# IF ($[QUERY.getGroupByList()] != 'null' AND $[QUERY.getGroupByList().size()] > '0') #}
{# IF ($[QUERY.getGroupByList()] != 'null' AND $[QUERY.getGroupByList().size()] > '0') #}{#NL#}
GROUP BY{#NL#}
{# LIST #}  $[QUERY.getGroupByList().foreach(getText())] {#SEP#}, {# ENDLIST #}
{# ENDIF #}
{# ENDIF #}
{# IF ($[QUERY.getHavingList()] != 'null' AND $[QUERY.getHavingList().size()] > '0')#}
{# IF ($[QUERY.getHavingList()] != 'null' AND $[QUERY.getHavingList().size()] > '0') #}{#NL#}
HAVING{#NL#}
{# LIST #}  $[QUERY.getHavingList().foreach(getText())] {#SEP#} AND {# ENDLIST #}
{# ENDIF #}
{# ENDIF #}
{# IF ($[QUERY.getOrderByList()] != 'null' AND $[QUERY.getOrderByList().size()] > '0') #}{#NL#}
ORDER BY{#NL#}
{# LIST #}  $[QUERY.getOrderByList()] {#SEP#}, {# ENDLIST #}
{# ENDIF #}
{# IF ($[QUERY.getSetOperation()] != 'null' AND $[QUERY.getSetOperation().length()] > '0') #} {#NL#}
  $[QUERY.getSetOperation()]{#NL#}
  ( $[QUERY.getSetOperand().getText()] )
{# ENDIF #}

$[JOIN.getLeftText()] $[JOIN.getJoinTypeText()] $[JOIN.getRightText()] 
{# IF ($[JOIN.getPredicateText()] != 'null' AND !$[JOIN.isCrossOrNatural()]) #} 
{#NL#}    ON  $[JOIN.getPredicateText()]{#NL#} {# ENDIF #}
    

$[TABLE.getFullGeneratedName()]

  TABLE ( $[TF.getFunctionName()] ({# FOR ($[TF.getParameterTypes()],$[TF.getParameters()]) IN ($[TYPE],$[PARAMETER]) SEP = ',  ' #}
  {# IF ($[TYPE] == 'SCALAR') #} $[PARAMETER] {# ELSE #} CURSOR($[PARAMETER]){# ENDIF #}{# ENDFOR #}
  ))

{#IF $[hasTableAlias]#}
$[ATTR.getSQLAccessName(TABLE_ALIAS)]
{#ELSE#}
$[ATTR.getSQLAccessName()]
{#ENDIF#}



  ------------------- Step 2 - -----------------

   

table_name = '$[statement.getStagingTableName()]';

sql = """
DECLARE
  uri_list CLOB;
  staging_table_name varchar2(200);
BEGIN
  dbms_lob.createtemporary(uri_list, TRUE);

  """
  uris.each{
  sql = sql + "dbms_lob.append(uri_list,'"+it+"'); \n"
  }

  sql = sql + """

  staging_table_name := '${table_name}';

  dbms_cloud.copy_data(
    schema_name => '$[statement.getStagingSchema()]',
{# IF ($[dynamicURIList] != 'true') #}
    table_name =>'$[statement.getStagingTableName()]',
    file_uri_list =>'{# FOR ($[statement.getResourceList()]) IN ($[RESOURCE]) SEP = ',' #}$[statement.getDirectory()]/o/$[RESOURCE]{# ENDFOR #}',
{# ELSE #}
    table_name => staging_table_name,
    file_uri_list => uri_list,
{# ENDIF #}
    credential_name =>'$[statement.getCredentialName()]',
{# IF ($[statement.getFieldsDefinitions()] != '') #}
    field_list => '$[statement.getFieldsDefinitions()]',
{# ENDIF #}
    format => json_object(
{# IF ($[statement.getFileFormat()]  == 'F') #}
    'delimiter' VALUE '',
    'recorddelimiter' VALUE '$[statement.getRecordSeparator()]',
  {# IF ($[statement.getTextDelimiter()]  != '') #}
    'quote' VALUE '$[statement.getTextDelimiter()]',
  {# ENDIF #}
{# ELSIF ($[statement.getFileFormat()]  == 'D') #}
    'delimiter' VALUE '$[statement.getFieldSeparator()]',
    'recorddelimiter' VALUE '$[statement.getRecordSeparator()]',
  {# IF ($[statement.getTextDelimiter()]  != '') #}
    'quote' VALUE '$[statement.getTextDelimiter()]',
  {# ENDIF #}
{# ELSIF ($[statement.getFileFormat()]  == 'CSV') #}
    'type' VALUE '$[statement.getFileFormat()]',
{# ENDIF #}
    'skipheaders' VALUE '$[statement.getSkipHeaders()]'{# IF (!$[statement.getFormatProperties().isEmpty()]) #},
    {# FOR ($[statement.getFormatProperties()]) IN ($[PROP]) SEP = ',
    ' #}$[PROP]{# ENDFOR #}{# ENDIF #}{# IF ($[statement.getFormatPropertiesPlus()] != '') #},
    $[statement.getFormatPropertiesPlus()]{# ENDIF #})
 );
  
END;
"""
odiRef.setSummaryMessage(sql)

if ( con == null ) {
    con = odiRef.getJDBCConnection( "DEST" )
}
try {
    stmt = con.createStatement()
    stmt.execute( sql )
} finally {
    if (stmt != null) { stmt.closeOnCompletion() }
}
  
            
            

{#NL#}
SELECT 
{# IF $[QUERY.isDistinct()] #}{#NL#}
  DISTINCT 
{# ENDIF #}
{# IF ($[QUERY.getAliasList()] != 'null') #}{#NL#}
{# LIST #}  $[QUERY.getSelectList().foreach(getText())] $[QUERY.getColumnAliasSeparator()] $[QUERY.getAliasList()] {# SEP #},{#NL#}{# ENDLIST #} 
{# ELSE #}{#NL#}
{# LIST #}  $[QUERY.getSelectList().foreach(getText())] {# SEP #},{#NL#}{# ENDLIST #}
{# ENDIF #} 
{#NL#}
{# IF $[QUERY.isConstantQuery()] #} 
{#NL#}
$[QUERY.getConstantFromClauseText()] 
{# ELSE #}FROM {#NL#}
{# LIST #}  $[QUERY.getFromList().foreach(getText())]{# SEP #} ,{#NL#} {# ENDLIST #} 
{# ENDIF #} 

{# IF ($[QUERY.getWhereList()] != 'null' AND $[QUERY.getWhereList().size()] > '0') #}{#NL#}
WHERE{#NL#}
{# LIST #}  ($[QUERY.getWhereList()]{#NL#}) {# SEP #}AND {# ENDLIST #}
{# ENDIF #}
{# IF ($[QUERY.getGroupByList()] != 'null' AND $[QUERY.getGroupByList().size()] > '0') #}
{# IF ($[QUERY.getGroupByList()] != 'null' AND $[QUERY.getGroupByList().size()] > '0') #}{#NL#}
GROUP BY{#NL#}
{# LIST #}  $[QUERY.getGroupByList().foreach(getText())] {#SEP#}, {# ENDLIST #}
{# ENDIF #}
{# ENDIF #}
{# IF ($[QUERY.getHavingList()] != 'null' AND $[QUERY.getHavingList().size()] > '0')#}
{# IF ($[QUERY.getHavingList()] != 'null' AND $[QUERY.getHavingList().size()] > '0') #}{#NL#}
HAVING{#NL#}
{# LIST #}  $[QUERY.getHavingList().foreach(getText())] {#SEP#} AND {# ENDLIST #}
{# ENDIF #}
{# ENDIF #}
{# IF ($[QUERY.getOrderByList()] != 'null' AND $[QUERY.getOrderByList().size()] > '0') #}{#NL#}
ORDER BY{#NL#}
{# LIST #}  $[QUERY.getOrderByList()] {#SEP#}, {# ENDLIST #}
{# ENDIF #}
{# IF ($[QUERY.getSetOperation()] != 'null' AND $[QUERY.getSetOperation().length()] > '0') #} {#NL#}
  $[QUERY.getSetOperation()]{#NL#}
  ( $[QUERY.getSetOperand().getText()] )
{# ENDIF #}

$[JOIN.getLeftText()] $[JOIN.getJoinTypeText()] $[JOIN.getRightText()] 
{# IF ($[JOIN.getPredicateText()] != 'null' AND !$[JOIN.isCrossOrNatural()]) #} 
{#NL#}    ON  $[JOIN.getPredicateText()]{#NL#} {# ENDIF #}
    

$[TABLE.getFullGeneratedName()]

  TABLE ( $[TF.getFunctionName()] ({# FOR ($[TF.getParameterTypes()],$[TF.getParameters()]) IN ($[TYPE],$[PARAMETER]) SEP = ',  ' #}
  {# IF ($[TYPE] == 'SCALAR') #} $[PARAMETER] {# ELSE #} CURSOR($[PARAMETER]){# ENDIF #}{# ENDFOR #}
  ))

{#IF $[hasTableAlias]#}
$[ATTR.getSQLAccessName(TABLE_ALIAS)]
{#ELSE#}
$[ATTR.getSQLAccessName()]
{#ENDIF#}
  
