# Write your MySQL query statement below
WITH n AS(
SELECT num
FROM Mynumbers
GROUP BY num
HAVING COUNT(num) = 1
)

SELECT max(num) as num
FROM n