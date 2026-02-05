SELECT actor_id, directoR_id FROM ActorDirector GROUP BY actor_id, director_id HAVING COUNT(*) >= 3;
