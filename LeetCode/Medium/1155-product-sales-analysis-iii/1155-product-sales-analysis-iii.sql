# Write your MySQL query statement below
SELECT product_id, year as first_year, quantity, price
FROM(
    SELECT
        product_id,
        quantity,
        price,
        year,
        RANK() OVER(PARTITION BY product_id ORDER BY year) as rn
    FROM Sales
) as t
WHERE t.rn = 1
