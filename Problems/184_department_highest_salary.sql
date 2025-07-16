SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (d.id, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)
;
