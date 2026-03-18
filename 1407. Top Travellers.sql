SELECT u.name AS name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users AS u LEFT JOIN Rides AS r ON u.id=r.user_id GROUP BY u.id, u.name ORDER BY SUM(r.distance) DESC, name ASC;
