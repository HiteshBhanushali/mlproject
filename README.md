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
