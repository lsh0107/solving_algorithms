SELECT 
    ROUND(
        SUM(
            CASE WHEN 
                DATEDIFF(a.event_date, t.min_date) = 1 THEN 1 ELSE 0 END
            ) 
            / 
            COUNT(DISTINCT t.player_id), 2
        ) 
        as fraction
FROM
    (SELECT
        player_id,
        min(event_date) as min_date
    FROM
        Activity
    GROUP BY 
        player_id) as t
JOIN
    Activity a
ON t.player_id = a.player_id
