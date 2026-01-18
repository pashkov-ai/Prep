SELECT E.employee_id, team_size
FROM Employee as E
LEFT JOIN
(SELECT team_id,
    COUNT(employee_id) as team_size
FROM Employee
GROUP BY team_id) as T
ON E.team_id = T.team_id

-- window function
SELECT 
    employee_id,
    count(*) over (Partition BY team_id) as team_size
FROM Employee