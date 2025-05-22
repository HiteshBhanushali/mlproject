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
