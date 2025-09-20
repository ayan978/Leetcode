# Write your MySQL query statement below
WITH RankedSalaries AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
    RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) As  salary_rank
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM RankedSalaries
WHERE salary_rank = 1;
