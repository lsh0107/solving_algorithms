# Write your MySQL query statement below
WITH tempt AS(
    SELECT COUNT(*) as cnt
    FROM Product    
),
t AS(
    SELECT customer_id, COUNT(DISTINCT(product_key)) as cnt
    FROM Customer
    GROUP BY customer_id
)
SELECT t.customer_id
FROM t, tempt
WHERE t.cnt = tempt.cnt