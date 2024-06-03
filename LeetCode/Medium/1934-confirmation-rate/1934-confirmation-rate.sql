# Write your MySQL query statement below
WITH tempt AS(
    SELECT s.user_id, c.action
    FROM Signups s
    LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
)

SELECT user_id, IFNULL(ROUND(AVG(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END), 2), 0) as confirmation_rate
FROM tempt
GROUP BY user_id