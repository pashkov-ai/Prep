SELECT
    user_id,
    SUM(price*quantity) as spending
FROM Sales
JOIN Product
ON Sales.product_id = Product.product_id
GROUP BY user_id
ORDER BY spending DESC, user_id ASC