# Write your MySQL query statement below
WITH SalaryCount as(
    SELECT id, salary, DENSE_RANK() OVER(ORDER BY salary DESC) as ranking FROM Employee
)

SELECT MAX(CASE WHEN ranking=2 THEN salary ELSE NULL END) AS SecondHighestSalary FROM SalaryCount;
