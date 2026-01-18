SELECT ABS(MAX(e.salary) - MAX(m.salary)) as salary_difference
FROM Salaries as e, Salaries as m
WHERE e.department = 'Engineering' AND m.department = 'Marketing'