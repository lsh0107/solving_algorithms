WITH c AS(
    SELECT COUNT(DISTINCT(user_id)) as user
    FROM Users
)

# Write your MySQL query statement below
SELECT r.contest_id, IFNULL(ROUND(COUNT(r.user_id)/c.user, 4)*100, 0) as percentage
FROM Register r, c c
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id