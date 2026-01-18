SELECT name, bonus
FROM Employee
LEFT JOIN Bonus
ON Employee.empId = Bonus.EmpId
WHERE bonus < 1000 OR bonus IS NULL