# Write your MySQL query statement below

SELECT e.name as name, b.bonus as bonus FROM employee e LEFT JOIN Bonus b ON e.empId=b.empId WHERE b.bonus<1000 OR b.bonus is NULL;
