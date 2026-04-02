# Write your MySQL query statement below
SELECT P.product_name, sum(O.unit) as unit
FROM Products as P
JOIN Orders as O
ON P.product_id = O.product_id
WHERE YEAR(O.order_date) = 2020 and MONTH(O.order_date) = 2
GROUP BY P.product_name
HAVING sum(O.unit) >= 100