# Write your MySQL query statement below
WITH tempt AS(
    SELECT a.product_id, a.start_date, a.end_date, a.price, b.purchase_date, b.units
    FROM Prices a
    LEFT JOIN UnitsSold b
    ON a.product_id = b.product_id AND b.purchase_date BETWEEN a.start_date AND a.end_date
    )
    
SELECT product_id, IFNULL(ROUND(SUM(price*units) / SUM(units), 2), 0) as average_price
FROM tempt
GROUP BY product_id