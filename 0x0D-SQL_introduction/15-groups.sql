-- A script that lists the number of records with the
-- same socre in the table second_table

SELECT score, COUNT(score) as 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC
