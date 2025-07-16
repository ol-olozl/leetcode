SELECT Employee, Department, Salary
FROM (
    SELECT e.name AS Employee, d.name AS Department, e.salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) ranks
WHERE rnk <= 3
;
