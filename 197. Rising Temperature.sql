# Write your MySQL query statement below

SELECT w2.id AS id FROM Weather w1 JOIN Weather w2 WHERE w1.id = w2.id - 1 AND w2.temperature > w1.temperature;
