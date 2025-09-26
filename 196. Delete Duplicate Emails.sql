-- Write your PostgreSQL query statement below
DELETE FROM Person WHERE id NOT IN(SELECT MIN(ID) FROM Person GROUP BY email);
