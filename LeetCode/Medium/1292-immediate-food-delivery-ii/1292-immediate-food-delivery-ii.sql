# Write your MySQL query statement below
SELECT 
    ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)*100, 2) as immediate_percentage
FROM(
    SELECT
        order_date,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date ASC) as datee,
        customer_pref_delivery_date
    FROM Delivery) as sub
WHERE sub.datee = 1
