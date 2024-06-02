# Write your MySQL query statement below
WITH tempt AS(
    SELECT a.project_id, a.employee_id, b.name, b.experience_years
    FROM Project a
    LEFT JOIN Employee b
    ON a.employee_id = b.employee_id)
    
SELECT project_id, IFNULL(ROUND(SUM(experience_years)/count(employee_id), 2), 0) as average_years
FROM tempt
GROUP BY project_id