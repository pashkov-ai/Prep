# Write your MySQL query statement below
select distinct P.product_id, P.product_name
from Product as P
inner join Sales as S
on P.product_id = S.product_id
group by P.product_id
having MIN(S.sale_date) >= '2019-01-01' and MAX(S.sale_date) <= '2019-03-31'