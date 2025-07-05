https://www.nobroker.in/property/1-bhk-apartment-for-lease-in-bhyandar-east--mumbai-for-rs-1500000/8a9f9184972bc7a401972bcb82f5003a/detail

SELECT 
  'Net CCONs: End of Period' AS Account,
  SUM(NVL(CCON.amt_1, 0) + NVL(PCON.amt_2, 0)) AS Amount,
  NVL(CCON.PERIOD_1, PCON.PERIOD_2) AS PERIOD_4
FROM 
(
  SELECT 
    gb.ledger_id AS LEDGER_ID_1,
    (NVL(SUM(gb.period_net_dr - gb.period_net_cr), 0) * -1) AS amt_1,
    gb.period_name AS PERIOD_1
  FROM 
    gl_balances gb,
    gl_code_combinations gcc,
    gl_ledgers gl
  WHERE
    gcc.code_combination_id = gb.code_combination_id
    AND gl.currency_code = gb.currency_code
    AND gl.ledger_id = gb.ledger_id
    AND gl.name = 'EXC USD GAAP LEDGER'
    AND gb.period_name = 'Jun-25'
    AND gcc.segment6 = 'BENWMAMGT'
    AND gcc.segment1 IN ('98001')
    AND gcc.segment3 IN (
      SELECT child FROM (
        SELECT 
          tree.parent_pk1_value AS parent,
          CONNECT_BY_ISLEAF AS IsLeaf,
          LEVEL AS lv,
          tree.pk1_start_value AS child
        FROM fnd_tree_node tree
        WHERE tree.tree_structure_code = 'GL_ACCT_FLEX'
          AND tree.tree_code = 'ACCOUNT' 
          AND tree.tree_version_id = (
            SELECT tree_version_id 
            FROM fnd_tree_version_vl
            WHERE tree_code = 'ACCOUNT'
              AND tree_version_name = 'ACCOUNT_CURRENT'
          )
        START WITH tree.pk1_start_value IN ('CCONHC')
        CONNECT BY PRIOR tree_node_id = parent_tree_node_id
      ) WHERE IsLeaf = 1
    )
  GROUP BY gb.period_name, gb.ledger_id
) CCON

FULL OUTER JOIN

(
  SELECT 
    gb.ledger_id AS LEDGER_ID_2,
    (NVL(SUM(gb.period_net_dr - gb.period_net_cr), 0) * -1) AS amt_2,
    gb.period_name AS PERIOD_2
  FROM 
    gl_balances gb,
    gl_code_combinations gcc,
    gl_ledgers gl
  WHERE
    gcc.code_combination_id = gb.code_combination_id
    AND gl.currency_code = gb.currency_code
    AND gl.ledger_id = gb.ledger_id
    AND gl.name = 'EXC USD GAAP LEDGER'
    AND gb.period_name = 'Jun-25'
    AND gcc.segment6 = 'BENWMAMGT'
    AND gcc.segment1 IN ('98001')
    AND gcc.segment3 IN (
      SELECT child FROM (
        SELECT 
          tree.parent_pk1_value AS parent,
          CONNECT_BY_ISLEAF AS IsLeaf,
          LEVEL AS lv,
          tree.pk1_start_value AS child
        FROM fnd_tree_node tree
        WHERE tree.tree_structure_code = 'GL_ACCT_FLEX'
          AND tree.tree_code = 'ACCOUNT' 
          AND tree.tree_version_id = (
            SELECT tree_version_id 
            FROM fnd_tree_version_vl
            WHERE tree_code = 'ACCOUNT'
              AND tree_version_name = 'ACCOUNT_CURRENT'
          )
        START WITH tree.pk1_start_value IN ('PCONHC')
        CONNECT BY PRIOR tree_node_id = parent_tree_node_id
      ) WHERE IsLeaf = 1
    )
  GROUP BY gb.period_name, gb.ledger_id
) PCON

ON CCON.PERIOD_1 = PCON.PERIOD_2

GROUP BY NVL(CCON.PERIOD_1, PCON.PERIOD_2);


888888888888888888888888888888888888888888888888888888
SELECT 
'Net CCONs: End of Period' as Account,
SUM(CCON.amt_1+PCON.amt_2) as Amount,
CCON.PERIOD_1 as PERIOD_4

FROM 
(
Select 
distinct 
gb.ledger_id AS LEDGER_ID_1,
(nvl(SUM(gb.period_net_dr - gb.period_net_cr),0)*-1) as amt_1,
gb.period_name Period_1
 FROM 
gl_balances gb,
gl_code_combinations gcc,
gl_ledgers gl
Where
gcc.code_combination_id = gb.code_combination_id
and gl.currency_code = gb.currency_code
and gl.ledger_id = gb.ledger_id
and gl.name='EXC USD GAAP LEDGER'
AND gb.period_name = 'Jun-25'
and gcc.SEGMENT6 = 'BENWMAMGT'
and gcc.segment1 in ('98001')
AND gcc.segment3
    in(select child from (
						SELECT tree.parent_pk1_value parent, CONNECT_BY_ISLEAF IsLeaf, level lv,
						tree.pk1_start_value child
						FROM fnd_tree_node tree
						WHERE tree.tree_structure_code = 'GL_ACCT_FLEX'
						AND tree.tree_code = 'ACCOUNT' 
						AND tree.tree_version_id = (select tree_version_id 
						from fnd_tree_version_vl
						where tree_code = 'ACCOUNT'
						and tree_version_name = 'ACCOUNT_CURRENT')
						START WITH tree.pk1_start_value in('CCONHC')-- Account num should be provided
						CONNECT BY prior tree_node_id = parent_tree_node_id)
 						where IsLeaf=1
)
group by gb.period_name, gb.ledger_id) CCON,

(
Select 
distinct 
gb.ledger_id AS LEDGER_ID_2,
(nvl(SUM(gb.period_net_dr - gb.period_net_cr),0)*-1)  as amt_2,
gb.period_name Period_2
 FROM 
gl_balances gb,
gl_code_combinations gcc,
gl_ledgers gl
Where
gcc.code_combination_id = gb.code_combination_id
and gl.currency_code = gb.currency_code
and gl.ledger_id = gb.ledger_id
and gl.name='EXC USD GAAP LEDGER'
AND gb.period_name = 'Jun-25'
and gcc.segment1 in ('98001')
and gcc.SEGMENT6 = 'BENWMAMGT'
AND gcc.segment3
    in(select child from (
						SELECT tree.parent_pk1_value parent, CONNECT_BY_ISLEAF IsLeaf, level lv,
						tree.pk1_start_value child
						FROM fnd_tree_node tree
						WHERE tree.tree_structure_code = 'GL_ACCT_FLEX'
						AND tree.tree_code = 'ACCOUNT' 
						AND tree.tree_version_id = (select tree_version_id 
						from fnd_tree_version_vl
						where tree_code = 'ACCOUNT'
						and tree_version_name = 'ACCOUNT_CURRENT')
						START WITH tree.pk1_start_value in('PCONHC')-- Account num should be provided
						CONNECT BY prior tree_node_id = parent_tree_node_id)
 						where IsLeaf=1
)
group by gb.period_name, gb.ledger_id) PCON
WHERE 
CCON.PERIOD_1 = PCON.PERIOD_2
GROUP BY CCON.PERIOD_1


===================
Select 
distinct 
'Month-Prev year' as metric,
'Benefit Expenses - RX Drugs COBRA' as ACCOUNT,
nvl(SUM(gb.period_net_dr - gb.period_net_cr),0) as amt,
gb.period_name
FROM
gl_balances gb,
gl_code_combinations gcc,
gl_ledgers gl

Where
gcc.code_combination_id = gb.code_combination_id
and gl.currency_code = gb.currency_code
and gl.ledger_id = gb.ledger_id
and gl.name='EXC USD GAAP LEDGER'
AND gb.period_name = 'Jul-23'
and gcc.segment1 in ('98001')
and gcc.SEGMENT8 = '958'
AND gcc.segment3 = '500070'
group by gb.period_name
============================================
'"410020"."ACCOUNT"{Detail}=410020~Company Contribution - Dental{Detail}' + '"400020"."ACCOUNT"{Detail}=400020~Participant Contribution - Dental{Detail}' - '"500020"."ACCOUNT"{Detail}=500020~Benefit Expenses - Dental{Detail}'

'"410040"."ACCOUNT"{Detail}=410040~Company Contribution - Medical{Detail}' + '"400044"."ACCOUNT"{Detail}=400044~Participant Contribution - Medical{Detail}' - '"500040"."ACCOUNT"{Detail}=500040~Benefit Expenses - Medical{Detail}'
---------------------
update EFS_DAL_TABLE_COUNT_VALIDATION
set filter_condition = "(project_id,OBJECT_VERSION_NUMBER) in  
(select a.PROJECT_ID, a.OBJECT_VERSION_NUMBER   from 
 ((
   SELECT
       PROJECT_ID,
       OBJECT_VERSION_NUMBER,
       ATTRIBUTE2_DATE,
       ATTRIBUTE1_DATE,
	   CREATION_DATE,
w_insert_dt,
       nvl(LAG(ATTRIBUTE2_DATE,1) OVER (PARTITION BY PROJECT_ID ORDER BY OBJECT_VERSION_NUMBER),'01-JAN-1900') AS PREV_AIS_IN_SERV_DT,
       nvl(LAG(ATTRIBUTE1_DATE,1) OVER (PARTITION BY PROJECT_ID ORDER BY OBJECT_VERSION_NUMBER),'01-JAN-1900') AS PREV_EST_IN_SERV_DT,
       MIN(OBJECT_VERSION_NUMBER) OVER (PARTITION BY PROJECT_ID ORDER BY CREATION_DATE) AS MIN_OBJ_VERSION_NUM
   FROM EFS_DATA_LAYER.EFS_PPM_AUDIT_HIST_LKP ) )a
WHERE
   (a.ATTRIBUTE2_DATE !=a.PREV_AIS_IN_SERV_DT
    OR a.ATTRIBUTE1_DATE != a.PREV_EST_IN_SERV_DT)  
AND a.OBJECT_VERSION_NUMBER != a.MIN_OBJ_VERSION_NUM 
and trunc(a.w_insert_dt)= trunc(sysdate))"
where raw_table_name = 'EFS_PPM_AUDIT_HIST_LKP';

================

select * from EFS_PPM_AUDIT_HIST_LKP where concat(concat(project_id,'~'),OBJECT_VERSION_NUMBER) in  
(select concat(concat(a.PROJECT_ID, '~'), a.OBJECT_VERSION_NUMBER)   from 
 ((
   SELECT
       PROJECT_ID,
       OBJECT_VERSION_NUMBER,
       ATTRIBUTE2_DATE,
       ATTRIBUTE1_DATE,
	   CREATION_DATE,
w_insert_dt,
       nvl(LAG(ATTRIBUTE2_DATE,1) OVER (PARTITION BY PROJECT_ID ORDER BY OBJECT_VERSION_NUMBER),'01-JAN-1900') AS PREV_AIS_IN_SERV_DT,
       nvl(LAG(ATTRIBUTE1_DATE,1) OVER (PARTITION BY PROJECT_ID ORDER BY OBJECT_VERSION_NUMBER),'01-JAN-1900') AS PREV_EST_IN_SERV_DT,
       MIN(OBJECT_VERSION_NUMBER) OVER (PARTITION BY PROJECT_ID ORDER BY CREATION_DATE) AS MIN_OBJ_VERSION_NUM
   FROM EFS_DATA_LAYER.EFS_PPM_AUDIT_HIST_LKP ) )a
WHERE
   (a.ATTRIBUTE2_DATE !=a.PREV_AIS_IN_SERV_DT
    OR a.ATTRIBUTE1_DATE != a.PREV_EST_IN_SERV_DT)  
AND a.OBJECT_VERSION_NUMBER != a.MIN_OBJ_VERSION_NUM 
and trunc(a.w_insert_dt)= trunc(sysdate));


======================================== Data Validation Procedure ===================================
create or replace PROCEDURE                  "EFS_PRC_CUSTOM_DATA_VALIDATION" 
authid current_user
AS 
BEGIN
DECLARE
    v_location_uri      VARCHAR2(100) := 'https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/';
    v_uri_list          VARCHAR2(4000) := 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/';
    v_credential_name   VARCHAR2(255);
    v_src_bkt_name          VARCHAR2(255);
    v_dest_bkt_name          VARCHAR2(255);
    v_file_name_filter  VARCHAR2(255);
    v_ext_file_extract       VARCHAR2(255):='BICC_BUCKET_ARCHIVAL';
    v_trunc_sql VARCHAR2(255);
    v_oos_namespace VARCHAR2(255);

BEGIN
--truncate table
v_trunc_sql := 'TRUNCATE TABLE ' ||'EFS_OOS_TO_RAW_COUNT';
EXECUTE IMMEDIATE v_trunc_sql;



v_trunc_sql := 'TRUNCATE TABLE ' || 'EFS_RAW_TABLE_COUNT';
EXECUTE IMMEDIATE v_trunc_sql;

v_trunc_sql := 'TRUNCATE TABLE ' ||'EFS_RAW_TABLE_COUNT_VALIDATION';
EXECUTE IMMEDIATE v_trunc_sql;

v_trunc_sql := 'TRUNCATE TABLE ' ||'EFS_DAL_TABLE_COUNT_VALIDATION';
EXECUTE IMMEDIATE v_trunc_sql;



v_trunc_sql := 'TRUNCATE TABLE ' || 'EFS_DAL_TABLE_COUNT';
EXECUTE IMMEDIATE v_trunc_sql;




--get credential_name



    SELECT
        credential_name
    INTO v_credential_name
    FROM
        user_credentials;
--get object storage bucket name,OSS_NAME_SPACE



select ARCHIVAL_SRC_BKT_NAME,ARCHIVAL_DEST_BKT_NAME ,OOS_NAMESPACE
into v_src_bkt_name,v_dest_bkt_name,v_oos_namespace
from EFS_RAW.EFS_EXT_FILE_LIST where EXT_FILE_EXTRACT =v_ext_file_extract;




--get actual and latest file name file name from object storage
FOR i in(
SELECT Distinct



                REPLACE(REPLACE(object_name,' ','%20'),'/','%2F') file_name



            FROM



                TABLE ( dbms_cloud.list_objects(credential_name => v_credential_name, location_uri => v_location_uri||v_oos_namespace||'/'|| v_dest_bkt_name



                                                                                                      || '/') )



            WHERE



                upper(object_name) LIKE upper('%JSON%') and trunc(last_modified)= trunc(SYSDATE))



    LOOP



      dbms_cloud.copy_data(table_name => 'EFS_OOS_TO_RAW_COUNT',



                                                                                                credential_name => v_credential_name,



                        file_uri_list => v_uri_list||v_oos_namespace||'/b/'||v_dest_bkt_name||'/o/'|| i.file_name,



                        format =>JSON_OBJECT('type' value 'json', 'columnpath' value '["$.statuses.name","$.statuses.rowCount","$.statuses.runDate"]')   );



    END LOOP;
END;



---RAW TABLES ROW COUNT
Declare 
v_sql_query CLOB;

BEGIN
For i in (Select distinct raw_table_name table_name, alias als from EFS_PVO_TO_RAW_TABLE_MAPPING)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
v_sql_query:= 'INSERT INTO EFS_RAW_TABLE_COUNT (Select ''' || i.table_name ||''', (Select count(1) from EFS_RAW.'||i.table_name||' where trunc(W_LOAD_DT)=trunc(SYSDATE)) row_count,SYSDATE,'''||i.als||''' from dual)';
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('NEW_DONE');
COMMIT;
END LOOP;
END;




---VALIDATING PVO WITH RAW
DECLARE 
BEGIN
insert into EFS_RAW_table_count_validation  (
Select A.PVO_NAME, B.RAW_TABLE_NAME, A.ROW_COUNT PVO_COUNT, C.ROW_COUNT RAW_TABLE_COUNT, CASE WHEN A.ROW_COUNT<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS RAW_COUNT_STATUS
,c.AS_OF_DATE from EFS_OOS_TO_RAW_COUNT A left join
EFS_PVO_TO_RAW_TABLE_MAPPING B on A.PVO_NAme=B.PVO_Name
left join EFS_RAW_TABLE_COUNT C on B. RAW_TABLE_NAME=C.RAW_Table_NAme);
--dbms_output.put_line('1');
COMMIT;
END;

--updating raw with filter condition
Declare 
v_sql_query CLOB;
BEGIN
For i in (Select raw_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where Filter_Condition <> '1=1' and SOURCE_DAL_TABLE is null)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
v_sql_query:= 'UPDATE EFS_RAW_TABLE_COUNT SET ROW_COUNT= (Select count(1) from EFS_RAW.'||i.table_name||' where trunc(W_LOAD_DT)=trunc(SYSDATE) and '||i.Filter_Condition ||' ) where ALIAS='''||i.als||''' and RAW_TABLE_NAME='''||i.table_name||'''' ;
--dbms_output.put_line(v_sql_query);
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;

Declare 
v_sql_query CLOB;
BEGIN
For i in (Select DISTINCT raw_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where Filter_Condition <> '1=1' and SOURCE_DAL_TABLE is null AND FULL_LOAD_STATUS='Y')
LOOP
DBMS_OUTPUT.PUT_LINE('TABLE'||i.table_name);
DBMS_OUTPUT.PUT_LINE('FILTER CONDITION '||i.Filter_Condition);
v_sql_query:= 'INSERT INTO EFS_RAW_TABLE_COUNT (Select ''' || i.table_name ||''', (Select count(1) from EFS_RAW.'||i.table_name||' where '||i.Filter_Condition||') row_count,SYSDATE,'''||i.als||''' from dual)';
--dbms_output.put_line(v_sql_query);
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;

---DAL TABLES ROW COUNT
Declare 
v_sql_query CLOB;
BEGIN
For i in (Select dal_table_name table_name,FULL_LOAD_STATUS from EFS_RAW_TO_DAL_MAPPING )
LOOP
DBMS_OUTPUT.PUT_LINE('TABLE '||i.table_name);
v_sql_query:= 'INSERT INTO EFS_DAL_TABLE_COUNT (Select ''' || i.table_name ||''', (Select count(1) from '||i.table_name||' where trunc(W_LOAD_DT)=trunc(SYSDATE) ) row_count,sysdate,0,'''||i.FULL_LOAD_STATUS||''' from dual)';
dbms_output.put_line('DONE');
EXECUTE IMMEDIATE v_sql_query;
COMMIT;
END LOOP;
END;




---VALIDATING RAW WITH DAL (FULL_LOAD)

BEGIN
insert into EFS_DAL_TABLE_COUNT_VALIDATION (
select D.Raw_Table_Name, D.DAL_TABLE_NAME, D.RAW_TABLE_COUNT+(case 
when D.DAL_TABLE_NAME='EFS_PPM_PROJECT_DIM' 
then (select count(*) from EFS_PPM_PROJECT_DIM where w_active_flag=0)
else 0
end
)as RAW_Table_Count,
C.ROW_COUNT DAL_TABLE_COUNT,
CASE WHEN D.RAW_TABLE_COUNT+(case 
when D.DAL_TABLE_NAME='EFS_PPM_PROJECT_DIM' 
then (select count(*) from EFS_PPM_PROJECT_DIM where w_active_flag=0)
else 0
end
)<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS DAL_COUNT_STATUS, D.Filter_Condition,c.AS_OF_DATE
from (Select A.Raw_Table_Name, B.DAL_TABLE_NAME, A.ROW_COUNT RAW_TABLE_COUNT,B.FULL_LOAD_STATUS,B.Alias, B.Filter_Condition
from EFS_RAW_TABLE_COUNT A left join
EFS_RAW_TO_DAL_MAPPING B on A.Alias=B.Alias where B.FULL_LOAD_STATUS ='Y') D
left join EFS_DAL_TABLE_COUNT C on D.DAL_TABLE_NAME=C.DAL_Table_NAme
where D.DAL_TABLE_NAME is not null and C.FULL_LOAD_STATUS='Y');
commit;
END;
---VALIDATING RAW WITH DAL (INCREMENTAL)

BEGIN
insert into EFS_DAL_TABLE_COUNT_VALIDATION (
select D.Raw_Table_Name, D.DAL_TABLE_NAME, D.RAW_TABLE_COUNT as RAW_Table_Count,
C.ROW_COUNT DAL_TABLE_COUNT,
CASE WHEN D.RAW_TABLE_COUNT<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS DAL_COUNT_STATUS, D.Filter_Condition,c.AS_OF_DATE
from (Select A.Raw_Table_Name, B.DAL_TABLE_NAME, A.ROW_COUNT RAW_TABLE_COUNT,B.FULL_LOAD_STATUS,B.Alias, B.Filter_Condition
from EFS_RAW_TABLE_COUNT A left join
EFS_RAW_TO_DAL_MAPPING B on A.Alias=B.Alias where B.FULL_LOAD_STATUS ='N') D
left join EFS_DAL_TABLE_COUNT C on D.DAL_TABLE_NAME=C.DAL_Table_NAme
where D.DAL_TABLE_NAME is not null and C.FULL_LOAD_STATUS='N');
commit;
END;

----VALIDATING DAL WITH DAL
Declare 
v_sql_query CLOB;
BEGIN
For i in (Select raw_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where SOURCE_DAL_TABLE is not null)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
    if i.table_name in ('EFS_PPM_PROJECT_STATUS_HIS_DIM') then
        v_sql_query:= 'UPDATE EFS_DAL_TABLE_COUNT SET SOURCE_DAL_COUNT= (Select count(1) from EFS_DATA_LAYER.'||i.table_name||' where '||i.Filter_Condition ||' ) where  DAL_TABLE_NAME='''||i.table_name||'''' ;
        --dbms_output.put_line(v_sql_query);
        EXECUTE IMMEDIATE v_sql_query;
    else
        v_sql_query:= 'UPDATE EFS_DAL_TABLE_COUNT SET SOURCE_DAL_COUNT= (Select count(1) from EFS_DATA_LAYER.'||i.table_name||' where trunc(W_INSERT_DT)=trunc(SYSDATE) and '||i.Filter_Condition ||' ) where  DAL_TABLE_NAME='''||i.table_name||'''' ;
        --dbms_output.put_line(v_sql_query);
        EXECUTE IMMEDIATE v_sql_query;
    end if;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;

Declare 
v_sql_query CLOB;
BEGIN
For i in (Select dal_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where SOURCE_DAL_TABLE is not null)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
v_sql_query:= 'UPDATE EFS_DAL_TABLE_COUNT SET ROW_COUNT= (Select count(1) from EFS_DATA_LAYER.'||i.table_name||' where trunc(W_INSERT_DT)=trunc(SYSDATE) ) where  DAL_TABLE_NAME='''||i.table_name||'''' ;
--dbms_output.put_line(v_sql_query);
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;


BEGIN
insert into EFS_DAL_TABLE_COUNT_VALIDATION (
Select A.dal_Table_Name, B.dal_Table_Name, A.SOURCE_DAL_COUNT SOURCE_DAL_TABLE_COUNT, C.ROW_COUNT TARGET_DAL_TABLE_COUNT,
CASE WHEN A.SOURCE_DAL_COUNT<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS DAL_COUNT_STATUS, B.Filter_Condition,c.AS_OF_DATE
from EFS_DAL_TABLE_COUNT A left join
EFS_RAW_TO_DAL_MAPPING B on A.DAL_TABLE_NAME=B.SOURCE_DAL_TABLE
left join EFS_DAL_TABLE_COUNT C on B. DAL_TABLE_NAME=C.DAL_Table_NAme
where B.DAL_TABLE_NAME is not null);
commit;
END;
END;

=================================================================================

https://chitrakutdhamtalgajarda.org/wp-content/uploads/2020/10/Bhusundi-Ramayan-Hindi.pdf
https://chitrakutdhamtalgajarda.org/wp-content/uploads/2020/10/Bhusundi-Ramayan-Gujarati.pdf
https://in.linkedin.com/in/samir-kumar-jha-32689529

WITH 
SAWITH0 AS (select sum(T575361.XLA_GLOBAL_AMOUNT) as c1,
     T625856.COMPANY_SEGMENT_NAME as c2,
     cast(T575361.EXPENDITURE_ITEM_ID as  VARCHAR ( 38 ) ) as c3,
     T3542.FISCAL_PERIOD_NAME as c4,
     T625867.ACCOUNT_SEGMENT as c5,
     T625877.PROJECT_SEGMENT_DESCRIPTION as c6,
     T625877.PROJECT_SEGMENT_NAME as c7,
     T625877.PROJECT_SEGMENT as c8,
     T634964.SOURCE_PROJECT as c9,
     T575361.EXPENDITURE_ITEM_ID as c11,
     T575361.TRANSACTION_SOURCE_ID as c12,
     T3542.FISCAL_PERIOD_SORT_KEY as c13,
     T3542.FISCAL_PERIOD_SET_NAME as c14,
     T625877.HIERARCHY_VALUESET_CODE as c15,
     T625856.COMPANY_SEGMENT as c16,
     T625856.HIERARCHY_VALUESET_CODE as c17,
     cast(T575361.TRANSACTION_SOURCE_ID as  VARCHAR ( 38 ) ) as c19
from 
     (
          (
               (
                    OAX$OAC.DW_FISCAL_DAY_D T3542 /* Dim_DW_FISCAL_DAY_D */  inner join (
                         (
                              OAX$OAC.DW_PROJECT_D T3792 /* Dim_DW_PROJECT_D */  left outer join EFS_DATA_LAYER.EFS_P2P_ALLOC_PROJECTS_DIM T634964 /* Project_Dim_DW_PROJECTS_D_TL_Dim_EFS_P2P_ALLOC_PROJECTS_DIM_extendDim */  On T3792.PROJECT_NUMBER = T634964.PROJECT) inner join OAX$OAC.DW_PROJECT_SLA_COST_CF_SEC T575361 /* Fact_DW_PROJECT_SLA_COST_CF */  On T3792.PROJECT_ID = T575361.PROJECT_ID) On T3542.FISCAL_DAY_DATE = T575361.XLA_ACCOUNTING_DATE and T3542.FISCAL_PERIOD_SET_NAME = T575361.FISCAL_PERIOD_SET_NAME and T3542.FISCAL_PERIOD_TYPE = T575361.FISCAL_PERIOD_TYPE and T3542.ADJUSTMENT_PERIOD_FLAG in ('N', '~NOVALUE~')) left outer join 
                    EFS_DATA_LAYER.EFS_PROJECT_DIMH T625877 /* Dim_Project_Alternate_Dim_EFS_PROJECT_DIMH_customDim */  On T575361.GL_SEGMENT6_VALUESET_CODE = T625877.HIERARCHY_VALUESET_CODE and T575361.GL_SEGMENT6 = T625877.PROJECT_SEGMENT) left outer join 
               EFS_DATA_LAYER.EFS_BALANCE_SEGMENT_CURRENT_V T625856 /* Dim_Balance_Segment_Current_Dim_EFS_BALANCE_SEGMENT_CURRENT_V_customDim */  On T575361.GL_BLNC_SGMNT_VALUESET_CODE = T625856.HIERARCHY_VALUESET_CODE and T575361.GL_BALANCING_SEGMENT = T625856.COMPANY_SEGMENT) left outer join 
          EFS_DATA_LAYER.EFS_ACCOUNT_DIMH T625867 /* Dim_Natural_Account_Alternate_Dim_EFS_ACCOUNT_DIMH_customDim */  On T575361.NATURAL_ACCOUNT_SEGMENT = T625867.ACCOUNT_SEGMENT and T575361.NTRL_ACNT_SGMNT_VALUESET_CODE = T625867.HIERARCHY_VALUESET_CODE
where  ( T625877.PROJECT_SEGMENT = 'XITEED730' and (T575361.EXPENDITURE_ITEM_ID in (4701694, 4756974)) ) 
group by T3542.FISCAL_PERIOD_SORT_KEY, T3542.FISCAL_PERIOD_NAME, T3542.FISCAL_PERIOD_SET_NAME, T575361.TRANSACTION_SOURCE_ID, T575361.EXPENDITURE_ITEM_ID, T625856.COMPANY_SEGMENT, T625856.COMPANY_SEGMENT_NAME, T625856.HIERARCHY_VALUESET_CODE, T625867.ACCOUNT_SEGMENT, T625877.HIERARCHY_VALUESET_CODE, T625877.PROJECT_SEGMENT, T625877.PROJECT_SEGMENT_NAME, T625877.PROJECT_SEGMENT_DESCRIPTION, T634964.SOURCE_PROJECT),
SAWITH1 AS (select  /*+ no_merge */  T6610.USER_TRANSACTION_SOURCE as c1,
     T6610.TRANSACTION_SOURCE_ID as c2
from 
     OAX$OAC.DW_PROJECT_TXN_SOURCE_TL T6610 /* Lookup_DW_PROJECT_TXN_SOURCE_TL */ 
where  ( T6610.LANGUAGE = 'US' ) ),
SAWITH2 AS (select D1.c1 as c1,
     D1.c2 as c2,
     D1.c3 as c3,
     D1.c4 as c4,
     D1.c5 as c5,
     D1.c6 as c6,
     D1.c7 as c7,
     D1.c8 as c8,
     D1.c9 as c9,
     nvl(D2.c1 , D1.c19) as c10,
     D1.c11 as c11,
     D1.c12 as c12,
     D1.c13 as c13,
     D1.c14 as c14,
     D1.c15 as c15,
     D1.c16 as c16,
     D1.c17 as c17
from 
     SAWITH0 D1 left outer join SAWITH1 D2 On  SYS_OP_MAP_NONNULL(D1.c12) = SYS_OP_MAP_NONNULL(D2.c2) ),
SAWITH3 AS (select D1.c1 as c1,
     D1.c2 as c2,
     D1.c3 as c3,
     D1.c4 as c4,
     D1.c5 as c5,
     D1.c6 as c6,
     D1.c7 as c7,
     D1.c8 as c8,
     D1.c9 as c9,
     D1.c10 as c10,
     D1.c11 as c11,
     D1.c12 as c12,
     D1.c13 as c13,
     D1.c14 as c14,
     D1.c15 as c15,
     D1.c16 as c16,
     D1.c17 as c17,
     D1.c18 as c18,
     D1.c19 as c19,
     D1.c20 as c20,
     D1.c21 as c21,
     D1.c22 as c22,
     D1.c23 as c23,
     D1.c24 as c24
from 
     (select 0 as c1,
               D1.c2 as c2,
               D1.c3 as c3,
               D1.c4 as c4,
               D1.c5 as c5,
               D1.c6 as c6,
               D1.c7 as c7,
               D1.c8 as c8,
               D1.c9 as c9,
               D1.c10 as c10,
               'Month' as c11,
               D1.c11 as c12,
               D1.c12 as c13,
               D1.c13 as c14,
               D1.c1 as c15,
               0 as c16,
               0 as c17,
               0 as c18,
               0 as c19,
               0 as c20,
               D1.c14 as c21,
               D1.c15 as c22,
               D1.c16 as c23,
               D1.c17 as c24,
               ROW_NUMBER() OVER (PARTITION BY D1.c2, D1.c3, D1.c4, D1.c5, D1.c6, D1.c7, D1.c8, D1.c9, D1.c11, D1.c12, D1.c13, D1.c14, D1.c15, D1.c16, D1.c17 ORDER BY D1.c2 ASC, D1.c3 ASC, D1.c4 ASC, D1.c5 ASC, D1.c6 ASC, D1.c7 ASC, D1.c8 ASC, D1.c9 ASC, D1.c11 ASC, D1.c12 ASC, D1.c13 ASC, D1.c14 ASC, D1.c15 ASC, D1.c16 ASC, D1.c17 ASC) as c25
          from 
               SAWITH2 D1
     ) D1
where  ( D1.c25 = 1 ) )
select D1.c1 as c1,
     D1.c2 as c2,
     D1.c3 as c3,
     D1.c4 as c4,
     D1.c5 as c5,
     D1.c6 as c6,
     D1.c7 as c7,
     D1.c8 as c8,
     D1.c9 as c9,
     D1.c10 as c10,
     D1.c11 as c11,
     D1.c12 as c12,
     D1.c13 as c13,
     D1.c14 as c14,
     D1.c15 as c15,
     D1.c16 as c16,
     D1.c17 as c17,
     D1.c18 as c18,
     D1.c19 as c19,
     D1.c20 as c20,
     D1.c21 as c21,
     D1.c22 as c22,
     D1.c23 as c23,
     D1.c24 as c24
from 
     SAWITH3 D1
order by c4, c6, c13, c12, c3, c10, c21, c14, c5, c22, c8, c7, c23, c2, c24, c9

===================================================================
https://www.naukri.com/job-listings-oracle-analytics-cloud-consultant-the-it-mind-kolkata-mumbai-new-delhi-hyderabad-pune-chennai-bengaluru-3-to-10-years-190225500886?src=jobsearchDesk&sid=17484366972547696&xp=4&px=1&nignbevent_src=jobsearchDeskGNB
https://www.naukri.com/job-listings-oracle-analytics-cloud-oac-consultant-best-hawk-infosystems-pvt-ltd-mumbai-new-delhi-pune-2-to-7-years-220525934217?src=jobsearchDesk&sid=17484366972547696&xp=3&px=1&nignbevent_src=jobsearchDeskGNB
https://www.naukri.com/job-listings-oracle-analytics-with-btp-otbi-fdi-xforia-technologies-hyderabad-bengaluru-greater-noida-4-to-9-years-060525035325?src=simjobsjd_bottom
https://www.naukri.com/job-listings-oac-odi-developer-ntt-data-information-processing-services-private-l-imited-hyderabad-1-to-2-years-080525913863?src=simjobsjd_rt
https://www.naukri.com/job-listings-oracle-cloud-technical-consultant-genpact-noida-hyderabad-bengaluru-5-to-10-years-210125013341?src=simjobsjd_rt

https://www.udemy.com/course/oracle-data-integrator-odi-12c-developer-course/?couponCode=CP130525

========================EY GDS 1st round =====================================
general ques - about project - checked
--------ODI -
how can we identify bottlenecks when table to table mapping is running slow? - checked 
different types of detection strategy present?--  checked 
any customization done using knowledge module?--  checked 
how can you implement a mapping to handle full load monthly data or delta records also? -- checked
types of scd and its examples? how do you know the records became inactive? -- checked
limitation in between odi on prem and odi market place? -- 50-50
CDC? diff between scd and cdc?types of scd -- 50-50
if you have 3 mappings, if 3rd mappings fails we want 1 and 2 mappings transaction to get rollback.- ans - disable the commit option for 1 and2 mapping
,accordingly it will handle the trnsaction.
if you have 3 mappings, if 2nd mapping fails but we still want to run 3rd mapping? how can u do it without using KO and error handling option.?
-- ans -- set it as yes in synchronous/asynchronous under properties panel. check this
 
 
-----------sql -
 
delete duplicate records? what are different ways to do it? - checked
hierarchy relationship of employee using sql query? -- gave a high level sol between mgr and emp
types of indexes i worked? diff between unique and PK index? -- checked
difference between btree and bitmap? -- checked
how do you do the stats gathering?-- checked
what all info comes under explain plan? -- checked
diff between rank, dense rank? -- checked
difference between view and mv? which is better for optimization? -- checked
can we perform delete inside view? if yes, then will it reflect on base table. -- 50-50
what if view contains multiple table joins?
 
-- 
CREATE VIEW dept_emp_view AS
SELECT d.department_id, d.department_name, e.employee_id, e.employee_name
FROM departments d
JOIN employees e ON d.department_id = e.department_id;
 
CREATE OR REPLACE TRIGGER dept_emp_view_delete
INSTEAD OF DELETE ON dept_emp_view
FOR EACH ROW
BEGIN
  DELETE FROM employees
  WHERE employee_id = :OLD.employee_id;
END;
 
DELETE FROM dept_emp_view
WHERE employee_id = 101;
 
if view consist of multiple tables joins, how we can delete the records? --- we can use instead of trigger
 
--plsql -
 
types of cursor? what are they? implicit and explicit cursor
write plsql code to commit transaction after every 10000 records? - 50-50
ans - 
DECLARE
  CURSOR emp_cursor IS
    SELECT employee_id, employee_name
    FROM employees;
 
  emp_id employees.employee_id%TYPE;
  emp_name employees.employee_name%TYPE;
  counter NUMBER := 0;
 
BEGIN
  OPEN emp_cursor;
  LOOP
    FETCH emp_cursor INTO emp_id, emp_name;
    EXIT WHEN emp_cursor%NOTFOUND;
 
    -- Process the record (example: update a column, insert into another table, etc.)
    -- For demonstration, we will just output the employee details
    DBMS_OUTPUT.PUT_LINE('Employee ID: ' || emp_id || ' Employee Name: ' || emp_name);
 
    counter := counter + 1;
 
    -- Commit after every 10,000 records
    IF counter = 10000 THEN
      COMMIT;
      counter := 0;  -- Reset the counter
    END IF;
  END LOOP;
 
  -- Final commit to ensure any remaining records are committed
  COMMIT;
 
  CLOSE emp_cursor;
END;
 
 
=====================EY GDS 2nd round ===========
why do you want to switch?
what major mapping components  u worked on?
limitation between on prem and cloud?
commit after every 20000 records?
suppose there are 3 mappings and i want them to rollback the transaction if any of them gets failed.
split component uses?
indexes and their use cases?
CDC?
different KM's used?
what all KM's used in loading file to table?
how we can optimize the file to table mapping if the src table bringing petabytes of data?
 
 
========================EY GDS 3rd round ============
ODI -
architecture of odi.
table to file
different KM's used so far
how to load incremental data coming within span of 2 mins in source.
parallel hint and append parallel nologging(defined baseline )
indexes and its use cases
cdc
what all KM's used for loading data
performance tuning ? different approaches?
execution plan, stats gather?
array fetch size?
what should be the approach for a mapping taking longer time?
in what aspect Java EE agent better than standand alone agent
which KM to be used to insert 50 millions of records in one go?
Database profiling?
 
 
SQL -
analytic function rank and dense rnk diff?
delete duplicate query?
different types of partitions and its use case?
 
PLSQL -
types of cursor? what are they?
SQL loader and External table?
 

https://www.linkedin.com/jobs/view/oracle-etl-developer-odi-obiee-at-kforce-inc-4211011888?trk=public_jobs_topcard-title
https://mx.linkedin.com/jobs/view/odi-sql-oac-obiee-at-oracle-4091608262?trk=public_jobs_topcard-title
https://uk.linkedin.com/jobs/view/oracle-reporting-platform-engineer-at-bank-of-england-4222825391?trk=public_jobs_topcard-title
https://in.linkedin.com/jobs/view/oracle-fusion-data-intelligence-platform-technical-consultant-at-talent-worx-4231017626?position=26&pageNum=0&refId=SDJTfrY%2BWG%2BzfyKv95N6tw%3D%3D&trackingId=1BPtXR5EjEhHytgEZj374w%3D%3D
https://in.linkedin.com/jobs/view/oac-odi-developer-at-ntt-data-north-america-4206575150?position=32&pageNum=0&refId=SDJTfrY%2BWG%2BzfyKv95N6tw%3D%3D&trackingId=w4NyHGsnsVQ1pZd7A%2FyR7g%3D%3D
https://www.linkedin.com/jobs/view/sr-oracle-analytics-engineer-at-net2source-inc-4230037095?trk=public_jobs_topcard-title
https://sg.linkedin.com/jobs/view/data-analytics-oac-obiee-at-randstad-singapore-4226083155?trk=public_jobs_topcard-title
https://in.linkedin.com/jobs/view/oac-faw-%2B-odi-consultant-at-apps-associates-4129624154?trk=public_jobs_topcard-title
https://uk.linkedin.com/jobs/view/oracle-reporting-platform-engineer-closing-date-28-may-2025-at-hackajob-4225461346?trk=public_jobs_topcard-title

case when  SUBSTRING("DFF - Project Costing Details"."PROJECTS_STD_COST_COLLECTION_WORK_ORDER_" FROM 1 FOR 1) = '[' then SUBSTRING("DFF - Project Costing Details"."PROJECTS_STD_COST_COLLECTION_WORK_ORDER_" FROM 2 FOR 8) else SUBSTRING("DFF - Project Costing Details"."PROJECTS_STD_COST_COLLECTION_WORK_ORDER_" FROM 1 FOR 8) end

create or replace PROCEDURE                  "COPY_EFS_PRC_CUSTOM_DATA_VALIDATION" 
authid current_user
AS 
BEGIN
DECLARE
    v_location_uri      VARCHAR2(100) := 'https://swiftobjectstorage.us-ashburn-1.oraclecloud.com/v1/';
    v_uri_list          VARCHAR2(4000) := 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/';
    v_credential_name   VARCHAR2(255);
    v_src_bkt_name          VARCHAR2(255);
    v_dest_bkt_name          VARCHAR2(255);
    v_file_name_filter  VARCHAR2(255);
    v_ext_file_extract       VARCHAR2(255):='BICC_BUCKET_ARCHIVAL';
    v_trunc_sql VARCHAR2(255);
    v_oos_namespace VARCHAR2(255);

BEGIN
--truncate table
v_trunc_sql := 'TRUNCATE TABLE ' ||'EFS_OOS_TO_RAW_COUNT';
EXECUTE IMMEDIATE v_trunc_sql;



v_trunc_sql := 'TRUNCATE TABLE ' || 'EFS_RAW_TABLE_COUNT';
EXECUTE IMMEDIATE v_trunc_sql;

v_trunc_sql := 'TRUNCATE TABLE ' ||'EFS_RAW_TABLE_COUNT_VALIDATION';
EXECUTE IMMEDIATE v_trunc_sql;

v_trunc_sql := 'TRUNCATE TABLE ' ||'EFS_DAL_TABLE_COUNT_VALIDATION';
EXECUTE IMMEDIATE v_trunc_sql;



v_trunc_sql := 'TRUNCATE TABLE ' || 'EFS_DAL_TABLE_COUNT';
EXECUTE IMMEDIATE v_trunc_sql;




--get credential_name



    SELECT
        credential_name
    INTO v_credential_name
    FROM
        user_credentials;
--get object storage bucket name,OSS_NAME_SPACE



select ARCHIVAL_SRC_BKT_NAME,ARCHIVAL_DEST_BKT_NAME ,OOS_NAMESPACE
into v_src_bkt_name,v_dest_bkt_name,v_oos_namespace
from EFS_RAW.EFS_EXT_FILE_LIST where EXT_FILE_EXTRACT =v_ext_file_extract;




--get actual and latest file name file name from object storage
FOR i in(
SELECT Distinct



                REPLACE(REPLACE(object_name,' ','%20'),'/','%2F') file_name



            FROM



                TABLE ( dbms_cloud.list_objects(credential_name => v_credential_name, location_uri => v_location_uri||v_oos_namespace||'/'|| v_dest_bkt_name



                                                                                                      || '/') )



            WHERE



                upper(object_name) LIKE upper('%JSON%') and trunc(last_modified)= trunc(SYSDATE))



    LOOP



      dbms_cloud.copy_data(table_name => 'EFS_OOS_TO_RAW_COUNT',



                                                                                                credential_name => v_credential_name,



                        file_uri_list => v_uri_list||v_oos_namespace||'/b/'||v_dest_bkt_name||'/o/'|| i.file_name,



                        format =>JSON_OBJECT('type' value 'json', 'columnpath' value '["$.statuses.name","$.statuses.rowCount","$.statuses.runDate"]')   );



    END LOOP;
END;



---RAW TABLES ROW COUNT
Declare 
v_sql_query CLOB;

BEGIN
For i in (Select distinct raw_table_name table_name, alias als from EFS_PVO_TO_RAW_TABLE_MAPPING)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
v_sql_query:= 'INSERT INTO EFS_RAW_TABLE_COUNT (Select ''' || i.table_name ||''', (Select count(1) from EFS_RAW.'||i.table_name||' where trunc(W_LOAD_DT)=trunc(SYSDATE)) row_count,SYSDATE,'''||i.als||''' from dual)';
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('NEW_DONE');
COMMIT;
END LOOP;
END;




---VALIDATING PVO WITH RAW
DECLARE 
BEGIN
insert into EFS_RAW_table_count_validation  (
Select A.PVO_NAME, B.RAW_TABLE_NAME, A.ROW_COUNT PVO_COUNT, C.ROW_COUNT RAW_TABLE_COUNT, CASE WHEN A.ROW_COUNT<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS RAW_COUNT_STATUS
,c.AS_OF_DATE from EFS_OOS_TO_RAW_COUNT A left join
EFS_PVO_TO_RAW_TABLE_MAPPING B on A.PVO_NAme=B.PVO_Name
left join EFS_RAW_TABLE_COUNT C on B. RAW_TABLE_NAME=C.RAW_Table_NAme);
--dbms_output.put_line('1');
COMMIT;
END;

--updating raw with filter condition
Declare 
v_sql_query CLOB;
BEGIN
For i in (Select raw_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where Filter_Condition <> '1=1' and SOURCE_DAL_TABLE is null)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
v_sql_query:= 'UPDATE EFS_RAW_TABLE_COUNT SET ROW_COUNT= (Select count(1) from EFS_RAW.'||i.table_name||' where trunc(W_LOAD_DT)=trunc(SYSDATE) and '||i.Filter_Condition ||' ) where ALIAS='''||i.als||''' and RAW_TABLE_NAME='''||i.table_name||'''' ;
--dbms_output.put_line(v_sql_query);
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;

Declare 
v_sql_query CLOB;
BEGIN
For i in (Select DISTINCT raw_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where Filter_Condition <> '1=1' and SOURCE_DAL_TABLE is null AND FULL_LOAD_STATUS='Y')
LOOP
DBMS_OUTPUT.PUT_LINE('TABLE'||i.table_name);
DBMS_OUTPUT.PUT_LINE('FILTER CONDITION '||i.Filter_Condition);
v_sql_query:= 'INSERT INTO EFS_RAW_TABLE_COUNT (Select ''' || i.table_name ||''', (Select count(1) from EFS_RAW.'||i.table_name||' where '||i.Filter_Condition||') row_count,SYSDATE,'''||i.als||''' from dual)';
--dbms_output.put_line(v_sql_query);
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;

---DAL TABLES ROW COUNT
Declare 
v_sql_query CLOB;
BEGIN
For i in (Select dal_table_name table_name,FULL_LOAD_STATUS from EFS_RAW_TO_DAL_MAPPING )
LOOP
DBMS_OUTPUT.PUT_LINE('TABLE '||i.table_name);
v_sql_query:= 'INSERT INTO EFS_DAL_TABLE_COUNT (Select ''' || i.table_name ||''', (Select count(1) from '||i.table_name||' where trunc(W_LOAD_DT)=trunc(SYSDATE) ) row_count,sysdate,0,'''||i.FULL_LOAD_STATUS||''' from dual)';
dbms_output.put_line('DONE');
EXECUTE IMMEDIATE v_sql_query;
COMMIT;
END LOOP;
END;




---VALIDATING RAW WITH DAL (FULL_LOAD)

BEGIN
insert into EFS_DAL_TABLE_COUNT_VALIDATION (
select D.Raw_Table_Name, D.DAL_TABLE_NAME, D.RAW_TABLE_COUNT+(case 
when D.DAL_TABLE_NAME='EFS_PPM_PROJECT_DIM' 
then (select count(*) from EFS_PPM_PROJECT_DIM where w_active_flag=0)
else 0
end
)as RAW_Table_Count,
C.ROW_COUNT DAL_TABLE_COUNT,
CASE WHEN D.RAW_TABLE_COUNT+(case 
when D.DAL_TABLE_NAME='EFS_PPM_PROJECT_DIM' 
then (select count(*) from EFS_PPM_PROJECT_DIM where w_active_flag=0)
else 0
end
)<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS DAL_COUNT_STATUS, D.Filter_Condition,c.AS_OF_DATE
from (Select A.Raw_Table_Name, B.DAL_TABLE_NAME, A.ROW_COUNT RAW_TABLE_COUNT,B.FULL_LOAD_STATUS,B.Alias, B.Filter_Condition
from EFS_RAW_TABLE_COUNT A left join
EFS_RAW_TO_DAL_MAPPING B on A.Alias=B.Alias where B.FULL_LOAD_STATUS ='Y') D
left join EFS_DAL_TABLE_COUNT C on D.DAL_TABLE_NAME=C.DAL_Table_NAme
where D.DAL_TABLE_NAME is not null and C.FULL_LOAD_STATUS='Y');
commit;
END;
---VALIDATING RAW WITH DAL (INCREMENTAL)

BEGIN
insert into EFS_DAL_TABLE_COUNT_VALIDATION (
select D.Raw_Table_Name, D.DAL_TABLE_NAME, D.RAW_TABLE_COUNT as RAW_Table_Count,
C.ROW_COUNT DAL_TABLE_COUNT,
CASE WHEN D.RAW_TABLE_COUNT<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS DAL_COUNT_STATUS, D.Filter_Condition,c.AS_OF_DATE
from (Select A.Raw_Table_Name, B.DAL_TABLE_NAME, A.ROW_COUNT RAW_TABLE_COUNT,B.FULL_LOAD_STATUS,B.Alias, B.Filter_Condition
from EFS_RAW_TABLE_COUNT A left join
EFS_RAW_TO_DAL_MAPPING B on A.Alias=B.Alias where B.FULL_LOAD_STATUS ='N') D
left join EFS_DAL_TABLE_COUNT C on D.DAL_TABLE_NAME=C.DAL_Table_NAme
where D.DAL_TABLE_NAME is not null and C.FULL_LOAD_STATUS='N');
commit;
END;

----VALIDATING DAL WITH DAL
Declare 
v_sql_query CLOB;
BEGIN
For i in (Select raw_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where SOURCE_DAL_TABLE is not null)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
v_sql_query:= 'UPDATE EFS_DAL_TABLE_COUNT SET SOURCE_DAL_COUNT= (Select count(1) from EFS_DATA_LAYER.'||i.table_name||' where trunc(W_INSERT_DT)=trunc(SYSDATE) and '||i.Filter_Condition ||' ) where  DAL_TABLE_NAME='''||i.table_name||'''' ;
--dbms_output.put_line(v_sql_query);
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;

Declare 
v_sql_query CLOB;
BEGIN
For i in (Select dal_table_name table_name,Filter_Condition Filter_Condition, ALIAS als from EFS_RAW_TO_DAL_MAPPING where SOURCE_DAL_TABLE is not null)
LOOP
DBMS_OUTPUT.PUT_LINE('TAB'||i.table_name);
v_sql_query:= 'UPDATE EFS_DAL_TABLE_COUNT SET ROW_COUNT= (Select count(1) from EFS_DATA_LAYER.'||i.table_name||' where trunc(W_INSERT_DT)=trunc(SYSDATE) ) where  DAL_TABLE_NAME='''||i.table_name||'''' ;
--dbms_output.put_line(v_sql_query);
EXECUTE IMMEDIATE v_sql_query;
DBMS_OUTPUT.PUT_LINE('DONE');
COMMIT;
END LOOP;
END;


BEGIN
insert into EFS_DAL_TABLE_COUNT_VALIDATION (
Select A.dal_Table_Name, B.dal_Table_Name, A.SOURCE_DAL_COUNT SOURCE_DAL_TABLE_COUNT, C.ROW_COUNT TARGET_DAL_TABLE_COUNT,
CASE WHEN A.SOURCE_DAL_COUNT<>C.ROW_COUNT THEN 'NOT MATCHING' ELSE 'MATCHING' END AS DAL_COUNT_STATUS, B.Filter_Condition,c.AS_OF_DATE
from EFS_DAL_TABLE_COUNT A left join
EFS_RAW_TO_DAL_MAPPING B on A.DAL_TABLE_NAME=B.SOURCE_DAL_TABLE
left join EFS_DAL_TABLE_COUNT C on B. DAL_TABLE_NAME=C.DAL_Table_NAme
where B.DAL_TABLE_NAME is not null);
commit;
END;
END;
