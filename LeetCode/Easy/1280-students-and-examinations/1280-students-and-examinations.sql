# Write your MySQL query statement below
WITH tempt AS(
    SELECT a.student_id, a.student_name, c.subject_name, COUNT(b.subject_name) as attended_exams
    FROM Students a
    CROSS JOIN Subjects c
    LEFT JOIN Examinations b
    ON a.student_id = b.student_id AND b.subject_name = c.subject_name
    GROUP BY a.student_id, a.student_name, c.subject_name)

SELECT * 
FROM tempt
ORDER BY student_id, subject_name