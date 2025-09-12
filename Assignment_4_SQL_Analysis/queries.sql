-- Q1: Find the total sales per store
SELECT s.store_name, 
       SUM(oi.list_price * oi.quantity) AS total_sales
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN stores s ON s.store_id = o.store_id
GROUP BY s.store_name;

-- Q2: Get the top 5 customers who spent the most money
SELECT TOP 5
    SUM(oi.list_price * oi.quantity) AS total_spent,
    c.first_name + ' ' + c.last_name AS customer_name
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.first_name, c.last_name
ORDER BY total_spent DESC;

-- Q3: List customers with no orders
SELECT *
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Q4: Top 3 staff based on orders quantity
SELECT TOP 3
    s.staff_id,
    s.first_name,
    s.last_name,
    SUM(oi.quantity) AS total_quantity
FROM staffs s
JOIN orders o ON s.staff_id = o.staff_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY s.staff_id, s.first_name, s.last_name
ORDER BY total_quantity DESC;
