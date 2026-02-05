SELECT ROUND(SUM(CASE WHEN a2.player_id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*),2) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) f
LEFT JOIN Activity a2
  ON a2.player_id = f.player_id
 AND a2.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);
