SELECT customer_id FROM (SELECT customer_id, COUNT(DISTINCT product_key) as pro_count FROM Customer GROUP BY customer_id) AS temp WHERE pro_count = (SELECT COUNT(*) FROM Product);
