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
