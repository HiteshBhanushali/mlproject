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
