# Write your MySQL query statement below
WITH tempt AS (
    SELECT a.empId, a.name, a.supervisor, a.salary, b.bonus
    FROM Employee a
    LEFT JOIN Bonus b 
    ON a.empId = b.empId)
    
SELECT name, bonus
FROM tempt
WHERE bonus < 1000 or bonus IS NULL