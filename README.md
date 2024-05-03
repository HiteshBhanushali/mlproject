##END to END Machine Learning Project
DECLARE
   v_random_char CHAR(1); -- Variable to hold the random character
BEGIN
   -- Loop through each row in your_table
   FOR rec IN (SELECT * FROM your_table) LOOP
      v_random_char := CHR(TRUNC(DBMS_RANDOM.VALUE(65, 90)));
      UPDATE your_table
      SET your_column = v_random_char
      WHERE primary_key_column = rec.primary_key_column; -- Replace primary_key_column with your table's primary key
   END LOOP;
END;


PROJECT_ID	PROJECT_NAME	TRANSACTION_IDG	CHART_OF_ACCOUNTS_ID	CODE_COMBINATION_ID	GAAP_ACCOUNT	FERC_ACCOUNT	TOTAL_CREDITS	TOTAL_DEBITS
AMTEST201	Test Project_12	13000	2001	28001	531031		31700	
AMTEST201	Test Project_12	13000	2001	28002	526020			4500
AMTEST201	Test Project_12	13000	2004	10006		000000	4700	
AMTEST201	Test Project_12	13000	2004	10007		000000		4700




select
 
ppab.segment1 AS  Project_Id,
 
ppat.name AS Project_Name,
 
PEIA.EXPENDITURE_ITEM_ID AS TRANSACTION_IDg,
 
-- gcc.CHART_OF_ACCOUNTS_ID,gcc.CODE_COMBINATION_ID,
 
CASE WHEN gcc.CHART_OF_ACCOUNTS_ID=2001 then 
gcc.segment3   else null end as GAAP_ACCOUNT,
CASE WHEN gcc.CHART_OF_ACCOUNTS_ID=2004 then 
gcc.segment3   else null end as FERC_ACCOUNT,
c.accounted_cr Total_Credits,
 
c.accounted_dr Total_Debits
 
from PJC_EXP_ITEMS_ALL peia,
 
PJC_COST_DIST_LINES_ALL PCDL,
 
PJF_PROJECTS_ALL_B ppab,
 
PJF_PROJECTS_ALL_TL ppat,
 
xla_distribution_links XDA ,
 
xla_ae_lines XAL ,
 
gl_code_combinations gcc,
 
GL_JE_BATCHES A,
 
GL_JE_HEADERS B,
 
GL_JE_LINES C
 
where
 
peia.expenditure_item_id=PCDL.expenditure_item_id (+)
 
AND pcdl.expenditure_item_id = xda.source_distribution_id_num_1
 
-- AND pcdl.acct_event_id (+)= xda.event_id
 
AND xda.ae_header_id = xal.ae_header_id
 
AND xda.ae_line_num = xal.ae_line_num
 
AND xal.code_combination_id = gcc.code_combination_id
 
and PEIA.EXPENDITURE_ITEM_ID = 13000
 
AND gcc.code_combination_id = c.code_combination_id
 
and B.NAME='01-03-2024 Miscellaneous Cost'
 
and A.JE_BATCH_ID=B.JE_BATCH_ID
 
and B.JE_HEADER_ID =C.JE_HEADER_ID
 
AND peia.project_id = ppab.project_id
 
AND ppab.project_id = ppat.project_id;


-------------------------------

SELECT
    ppat.name AS Project_Name,
    PEIA.EXPENDITURE_ITEM_ID AS TRANSACTION_IDG,
    MAX(CASE WHEN gcc.CHART_OF_ACCOUNTS_ID = gaap_coa_id THEN gcc.segment3 ELSE NULL END) AS GAAP_ACCOUNT,
    MAX(CASE WHEN gcc.CHART_OF_ACCOUNTS_ID = ferc_coa_id THEN gcc.segment3 ELSE NULL END) AS FERC_ACCOUNT,
    SUM(CASE WHEN gcc.CHART_OF_ACCOUNTS_ID = gaap_coa_id THEN xal.accounted_cr ELSE 0 END) AS GAAP_CREDIT,
    SUM(CASE WHEN gcc.CHART_OF_ACCOUNTS_ID = gaap_coa_id THEN xal.accounted_dr ELSE 0 END) AS GAAP_DEBITS,
    SUM(CASE WHEN gcc.CHART_OF_ACCOUNTS_ID = ferc_coa_id THEN xal.accounted_cr ELSE 0 END) AS FERC_CREDIT,
    SUM(CASE WHEN gcc.CHART_OF_ACCOUNTS_ID = ferc_coa_id THEN xal.accounted_dr ELSE 0 END) AS FERC_DEBITS
FROM
    PJC_EXP_ITEMS_ALL peia
LEFT JOIN
    PJC_COST_DIST_LINES_ALL PCDL ON peia.expenditure_item_id = PCDL.expenditure_item_id
LEFT JOIN
    xla_distribution_links XDA ON PCDL.expenditure_item_id = XDA.source_distribution_id_num_1
LEFT JOIN
    xla_ae_lines XAL ON XDA.ae_header_id = XAL.ae_header_id AND XDA.ae_line_num = XAL.ae_line_num
LEFT JOIN
    gl_code_combinations gcc ON XAL.code_combination_id = gcc.code_combination_id
LEFT JOIN
    GL_JE_BATCHES A ON XAL.je_batch_id = A.je_batch_id
LEFT JOIN
    GL_JE_HEADERS B ON A.je_header_id = B.je_header_id
LEFT JOIN
    GL_JE_LINES C ON B.je_header_id = C.je_header_id AND gcc.code_combination_id = C.code_combination_id
LEFT JOIN
    PJF_PROJECTS_ALL_B ppab ON peia.project_id = ppab.project_id
LEFT JOIN
    PJF_PROJECTS_ALL_TL ppat ON ppab.project_id = ppat.project_id
LEFT JOIN
    (SELECT DISTINCT CHART_OF_ACCOUNTS_ID AS gaap_coa_id FROM gl_code_combinations WHERE <condition for GAAP account>) AS gaap_coa
    ON 1=1
LEFT JOIN
    (SELECT DISTINCT CHART_OF_ACCOUNTS_ID AS ferc_coa_id FROM gl_code_combinations WHERE <condition for FERC account>) AS ferc_coa
    ON 1=1
WHERE
    peia.expenditure_item_id = 13000
    AND B.NAME = '01-03-2024 Miscellaneous Cost'
GROUP BY
    ppat.name,
    PEIA.EXPENDITURE_ITEM_ID;
