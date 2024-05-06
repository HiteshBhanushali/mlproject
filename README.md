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
    Project_Name,
    TRANSACTION_IDG,
    GAAP_ACCOUNT,
    FERC_ACCOUNT,
    GAAP_CREDIT,
    GAAP_DEBITS,
    FERC_CREDIT,
    FERC_DEBITS
FROM
    (
        SELECT
            ppat.name AS Project_Name,
            PEIA.EXPENDITURE_ITEM_ID AS TRANSACTION_IDG,
            gcc.segment3 AS GAAP_ACCOUNT,
            NULL AS FERC_ACCOUNT,
            c.accounted_cr AS GAAP_CREDIT,
            c.accounted_dr AS GAAP_DEBITS,
            NULL AS FERC_CREDIT,
            NULL AS FERC_DEBITS
        FROM
            PJC_EXP_ITEMS_ALL peia,
            PJC_COST_DIST_LINES_ALL PCDL,
            xla_distribution_links XDA,
            xla_ae_lines XAL,
            gl_code_combinations gcc,
            GL_JE_LINES c,
            GL_JE_HEADERS B,
            PJF_PROJECTS_ALL_B ppab,
            PJF_PROJECTS_ALL_TL ppat
        WHERE
            peia.expenditure_item_id = PCDL.expenditure_item_id (+)
            AND PCDL.expenditure_item_id = XDA.source_distribution_id_num_1 (+)
            AND XDA.ae_header_id = XAL.ae_header_id (+)
            AND XDA.ae_line_num = XAL.ae_line_num (+)
            AND XAL.code_combination_id = gcc.code_combination_id (+)
            AND gcc.code_combination_id = c.code_combination_id (+)
            AND c.je_header_id = B.je_header_id (+)
            AND peia.project_id = ppab.project_id (+)
            AND ppab.project_id = ppat.project_id (+)
            AND peia.expenditure_item_id = 13000
            AND B.name = '01-03-2024 Miscellaneous Cost'
            AND c.name LIKE 'GAAP%'

        UNION ALL

        SELECT
            ppat.name AS Project_Name,
            PEIA.EXPENDITURE_ITEM_ID AS TRANSACTION_IDG,
            NULL AS GAAP_ACCOUNT,
            gcc.segment3 AS FERC_ACCOUNT,
            NULL AS GAAP_CREDIT,
            NULL AS GAAP_DEBITS,
            c.accounted_cr AS FERC_CREDIT,
            c.accounted_dr AS FERC_DEBITS
        FROM
            PJC_EXP_ITEMS_ALL peia,
            PJC_COST_DIST_LINES_ALL PCDL,
            xla_distribution_links XDA,
            xla_ae_lines XAL,
            gl_code_combinations gcc,
            GL_JE_LINES c,
            GL_JE_HEADERS B,
            PJF_PROJECTS_ALL_B ppab,
            PJF_PROJECTS_ALL_TL ppat
        WHERE
            peia.expenditure_item_id = PCDL.expenditure_item_id (+)
            AND PCDL.expenditure_item_id = XDA.source_distribution_id_num_1 (+)
            AND XDA.ae_header_id = XAL.ae_header_id (+)
            AND XDA.ae_line_num = XAL.ae_line_num (+)
            AND XAL.code_combination_id = gcc.code_combination_id (+)
            AND gcc.code_combination_id = c.code_combination_id (+)
            AND c.je_header_id = B.je_header_id (+)
            AND peia.project_id = ppab.project_id (+)
            AND ppab.project_id = ppat.project_id (+)
            AND peia.expenditure_item_id = 13000
            AND B.name = '01-03-2024 Miscellaneous Cost'
            AND c.name LIKE 'FERC%'
    ) AS CombinedData
ORDER BY
    TRANSACTION_IDG, GAAP_ACCOUNT, FERC_ACCOUNT;



    -=------------------------------------------- TRY -----------------------
    SELECT
    ppat.name AS Project_Name,
    PEIA.EXPENDITURE_ITEM_ID AS TRANSACTION_IDG,
    MAX(CASE WHEN c.name LIKE 'GAAP%' THEN gcc.segment3 END) AS GAAP_ACCOUNT,
    MAX(CASE WHEN c.name LIKE 'FERC%' THEN gcc.segment3 END) AS FERC_ACCOUNT,
    MAX(CASE WHEN c.name LIKE 'GAAP%' THEN c.accounted_cr END) AS GAAP_CREDIT,
    MAX(CASE WHEN c.name LIKE 'GAAP%' THEN c.accounted_dr END) AS GAAP_DEBITS,
    MAX(CASE WHEN c.name LIKE 'FERC%' THEN c.accounted_cr END) AS FERC_CREDIT,
    MAX(CASE WHEN c.name LIKE 'FERC%' THEN c.accounted_dr END) AS FERC_DEBITS
FROM
    PJC_EXP_ITEMS_ALL peia
    LEFT JOIN PJC_COST_DIST_LINES_ALL PCDL ON peia.expenditure_item_id = PCDL.expenditure_item_id
    LEFT JOIN xla_distribution_links XDA ON PCDL.expenditure_item_id = XDA.source_distribution_id_num_1
    LEFT JOIN xla_ae_lines XAL ON XDA.ae_header_id = XAL.ae_header_id AND XDA.ae_line_num = XAL.ae_line_num
    LEFT JOIN gl_code_combinations gcc ON XAL.code_combination_id = gcc.code_combination_id
    LEFT JOIN GL_JE_LINES c ON gcc.code_combination_id = c.code_combination_id
    LEFT JOIN GL_JE_HEADERS B ON c.je_header_id = B.je_header_id
    LEFT JOIN PJF_PROJECTS_ALL_B ppab ON peia.project_id = ppab.project_id
    LEFT JOIN PJF_PROJECTS_ALL_TL ppat ON ppab.project_id = ppat.project_id
WHERE
    peia.expenditure_item_id = 13000
    AND B.name = '01-03-2024 Miscellaneous Cost'
    AND (c.name LIKE 'GAAP%' OR c.name LIKE 'FERC%')
GROUP BY
    ppat.name,
    PEIA.EXPENDITURE_ITEM_ID;

