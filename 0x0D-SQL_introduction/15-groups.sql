-- A script that lists the number of records with the
-- same socre in the table second_table

SELECT DISTINCT score, COUNT(score) as 'number'
FROM second_table
GROUP BY score;
