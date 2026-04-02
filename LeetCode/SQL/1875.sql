select employee_id, name, salary,
    DENSE_RANK() over (order by salary) as team_id
from (
    select *,
        COUNT(*) over (partition by salary) as team_size
    from Employees
) as t
where team_size > 1
order by team_id, employee_id