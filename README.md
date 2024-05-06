Current Output							
PROJECT_NAME	TRANSACTION_IDG	GAAP_ACC	GAAP_CREDIT	GAAP_DEBIT			
POW POET FUT04 PJ14	31005	184175	223				
POW POET FUT04 PJ14	31005	510050		223			
							
PROJECT_NAME	TRANSACTION_IDG	FERC_ACC	FERC_CREDIT	FERC_DEBIT			
POW POET FUT04 PJ14	31005	000000	223				
POW POET FUT04 PJ14	31005	859001		223			
							
							
Required OUTPUT							
PROJECT_NAME	TRANSACTION_IDG	GAAP_ACC	GAAP_CREDIT	GAAP_DEBIT	FERC_ACC	FERC_CREDIT	FERC_DEBIT
POW POET FUT04 PJ14	31005	184175	223		000000	223	
POW POET FUT04 PJ14	31005	510050		223	859001		223

    ---------------------------------------------

##END to END Machine Learning Project

===============================
SELECT
    Project_Name,
    TRANSACTION_IDG,
    GAAP_ACCOUNT,
    FERC_ACCOUNT,
    MAX(GAAP_CREDIT) AS GAAP_CREDIT,
    MAX(GAAP_DEBITS) AS GAAP_DEBITS,
    MAX(FERC_CREDIT) AS FERC_CREDIT,
    MAX(FERC_DEBITS) AS FERC_DEBITS
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
            PJC_EXP_ITEMS_ALL peia
            LEFT JOIN PJC_COST_DIST_LINES_ALL PCDL ON peia.expenditure_item_id = PCDL.expenditure_item_id
            LEFT JOIN xla_distribution_links XDA ON PCDL.expenditure_item_id = XDA.source_distribution_id_num_1
            LEFT JOIN xla_ae_lines XAL ON XDA.ae_header_id = XAL.ae_header_id AND XDA.ae_line_num = XAL.ae_line_num
            LEFT JOIN gl_code_combinations gcc ON XAL.code_combination_id = gcc.code_combination_id
            LEFT JOIN GL_JE_LINES c ON gcc.code_combination_id = c.code_combination_id
            LEFT JOIN GL_JE_HEADERS B ON c.je_header_id = B.je_header_id
            LEFT JOIN PJF_PROJECTS_ALL_B ppab ON peia.project_id = ppab.project_id
            LEFT JOIN PJF_PROJECTS_ALL_TL ppat ON ppab.project_id = ppat.project_id
            LEFT JOIN gl_ledgers d ON B.ledger_id = d.ledger_id
        WHERE 
            peia.expenditure_item_id = 13000 
            AND B.name = '01-03-2024 Miscellaneous Cost' 
            AND d.name LIKE '%GAAP%'

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
            PJC_EXP_ITEMS_ALL peia
            LEFT JOIN PJC_COST_DIST_LINES_ALL PCDL ON peia.expenditure_item_id = PCDL.expenditure_item_id
            LEFT JOIN xla_distribution_links XDA ON PCDL.expenditure_item_id = XDA.source_distribution_id_num_1
            LEFT JOIN xla_ae_lines XAL ON XDA.ae_header_id = XAL.ae_header_id AND XDA.ae_line_num = XAL.ae_line_num
            LEFT JOIN gl_code_combinations gcc ON XAL.code_combination_id = gcc.code_combination_id
            LEFT JOIN GL_JE_LINES c ON gcc.code_combination_id = c.code_combination_id
            LEFT JOIN GL_JE_HEADERS B ON c.je_header_id = B.je_header_id
            LEFT JOIN PJF_PROJECTS_ALL_B ppab ON peia.project_id = ppab.project_id
            LEFT JOIN PJF_PROJECTS_ALL_TL ppat ON ppab.project_id = ppat.project_id
            LEFT JOIN gl_ledgers d ON B.ledger_id = d.ledger_id
        WHERE 
            peia.expenditure_item_id = 13000 
            AND B.name = '01-03-2024 Miscellaneous Cost' 
            AND d.name LIKE '%FERC%'
    ) CombinedData
GROUP BY
    Project_Name,
    TRANSACTION_IDG,
    GAAP_ACCOUNT,
    FERC_ACCOUNT
ORDER BY
    TRANSACTION_IDG, GAAP_ACCOUNT, FERC_ACCOUNT;

---==============================================================

Current output							
PROJECT_ID	TRANSACTION_IDG	GAAP_ACC	FERC_ACC	GAAP_CREDIT	GAAP_DEBIT	FERC_CREDIT	FERC_DEBIT
Test Project_12	13000	526020			4500		
Test Project_12	13000	531031		31700			
Test Project_12	13000		0			4700	
Test Project_12	13000		0				4700
							
Required Output							
PROJECT_ID	TRANSACTION_IDG	GAAP_ACC	FERC_ACC	GAAP_CREDIT	GAAP_DEBIT	FERC_CREDIT	FERC_DEBIT
Test Project_12	13000	526020			4500	4700	
Test Project_12	13000	531031		31700			4700

========================
SELECT
    Project_Name,
    TRANSACTION_IDG,
    GAAP_ACCOUNT,
    FERC_ACCOUNT,
    MAX(GAAP_CREDIT) AS GAAP_CREDIT,
    MAX(GAAP_DEBIT) AS GAAP_DEBIT,
    MAX(FERC_CREDIT) AS FERC_CREDIT,
    MAX(FERC_DEBIT) AS FERC_DEBIT
FROM
    (
        SELECT 
            ppat.name AS Project_Name, 
            PEIA.EXPENDITURE_ITEM_ID AS TRANSACTION_IDG, 
            gcc.segment3 AS GAAP_ACCOUNT, 
            NULL AS FERC_ACCOUNT, 
            SUM(CASE WHEN c.accounted_cr IS NOT NULL THEN c.accounted_cr ELSE 0 END) AS GAAP_CREDIT,
            SUM(CASE WHEN c.accounted_dr IS NOT NULL THEN c.accounted_dr ELSE 0 END) AS GAAP_DEBIT,
            NULL AS FERC_CREDIT,
            NULL AS FERC_DEBIT
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
            LEFT JOIN gl_ledgers d ON B.ledger_id = d.ledger_id
        WHERE 
            peia.expenditure_item_id = 13000 
            AND B.name = '01-03-2024 Miscellaneous Cost' 
            AND d.name LIKE '%GAAP%'
        GROUP BY
            ppat.name, 
            PEIA.EXPENDITURE_ITEM_ID, 
            gcc.segment3

        UNION ALL

        SELECT 
            ppat.name AS Project_Name, 
            PEIA.EXPENDITURE_ITEM_ID AS TRANSACTION_IDG, 
            NULL AS GAAP_ACCOUNT, 
            gcc.segment3 AS FERC_ACCOUNT,
            NULL AS GAAP_CREDIT,
            NULL AS GAAP_DEBIT,
            SUM(CASE WHEN c.accounted_cr IS NOT NULL THEN c.accounted_cr ELSE 0 END) AS FERC_CREDIT,
            SUM(CASE WHEN c.accounted_dr IS NOT NULL THEN c.accounted_dr ELSE 0 END) AS FERC_DEBIT
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
            LEFT JOIN gl_ledgers d ON B.ledger_id = d.ledger_id
        WHERE 
            peia.expenditure_item_id = 13000 
            AND B.name = '01-03-2024 Miscellaneous Cost' 
            AND d.name LIKE '%FERC%'
        GROUP BY
            ppat.name, 
            PEIA.EXPENDITURE_ITEM_ID, 
            gcc.segment3
    ) CombinedData
GROUP BY
    Project_Name,
    TRANSACTION_IDG,
    GAAP_ACCOUNT,
    FERC_ACCOUNT
ORDER BY
    TRANSACTION_IDG, GAAP_ACCOUNT, FERC_ACCOUNT;

============2345345========================
-- Select clause for GAAP columns
WITH GAAP_Data AS (
    SELECT 
        ppat.name AS Project_Name,
        peia.expenditure_item_id AS TRANSACTION_IDG,
        gcc.segment3 AS GAAP_ACC,
        c.accounted_cr AS GAAP_CREDIT,
        c.accounted_dr AS GAAP_DEBIT
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
        LEFT JOIN gl_ledgers d ON B.ledger_id = d.ledger_id
    WHERE 
        peia.expenditure_item_id = 13000 
        AND B.name = '01-03-2024 Miscellaneous Cost' 
        AND d.name LIKE '%GAAP%'
),
-- Select clause for FERC columns
FERC_Data AS (
    SELECT 
        ppat.name AS Project_Name,
        peia.expenditure_item_id AS TRANSACTION_IDG,
        gcc.segment3 AS FERC_ACC,
        c.accounted_cr AS FERC_CREDIT,
        c.accounted_dr AS FERC_DEBIT
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
        LEFT JOIN gl_ledgers d ON B.ledger_id = d.ledger_id
    WHERE 
        peia.expenditure_item_id = 13000 
        AND B.name = '01-03-2024 Miscellaneous Cost' 
        AND d.name LIKE '%FERC%'
)
-- Joining GAAP and FERC data based on TRANSACTION_IDG
SELECT
    COALESCE(G.Project_Name, F.Project_Name) AS Project_Name,
    COALESCE(G.TRANSACTION_IDG, F.TRANSACTION_IDG) AS TRANSACTION_IDG,
    G.GAAP_ACC,
    F.FERC_ACC,
    G.GAAP_CREDIT,
    G.GAAP_DEBIT,
    F.FERC_CREDIT,
    F.FERC_DEBIT
FROM
    GAAP_Data G
FULL OUTER JOIN FERC_Data F ON G.TRANSACTION_IDG = F.TRANSACTION_IDG
        AND G.GAAP_ACC = F.GAAP_ACC
ORDER BY
    COALESCE(G.TRANSACTION_IDG, F.TRANSACTION_IDG),
    G.GAAP_ACC;

