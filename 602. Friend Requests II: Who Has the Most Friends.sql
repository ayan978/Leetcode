# Write your MySQL query statement below

WITH all_edges AS (
  SELECT requester_id AS id, accepter_id AS friend_id FROM RequestAccepted
  UNION ALL
  SELECT accepter_id AS id, requester_id AS friend_id FROM RequestAccepted
),
friend_counts AS (
  SELECT id, COUNT(DISTINCT friend_id) AS num
  FROM all_edges
  GROUP BY id
)
SELECT id, num
FROM friend_counts
ORDER BY num DESC, id ASC
LIMIT 1;
