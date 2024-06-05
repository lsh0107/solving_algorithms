# Write your MySQL query statement below
SELECT s1.employee_id, s1.name, COUNT(s2.reports_to) as reports_count, ROUND(AVG(s2.age), 0) as average_age
FROM Employees s1
LEFT JOIN Employees s2
ON s1.employee_id = s2.reports_to
GROUP BY s1.employee_id
HAVING reports_count >= 1
ORDER BY 1