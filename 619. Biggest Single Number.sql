SELECT MAX(num) as num FROM (SELECT num, COUNT(num) AS num_count FROM MyNumbers GROUP BY num) AS tempTable WHERE num_count=1;
