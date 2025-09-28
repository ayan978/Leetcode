# Write your MySQL query statement below

SELECT w2.id AS id FROM Weather w1 JOIN Weather w2 WHERE w2.recordDate = w1.recordDate + INTERVAL 1 DAY AND w2.temperature > w1.temperature;
