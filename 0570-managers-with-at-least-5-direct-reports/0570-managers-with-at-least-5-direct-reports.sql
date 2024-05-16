# Write your MySQL query statement below
SELECT b.name
FROM Employee a
JOIN Employee b
ON a.managerID = b.id
GROUP BY a.managerID
HAVING count(a.managerID) >= 5