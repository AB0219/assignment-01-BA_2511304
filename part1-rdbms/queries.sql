--Answers

--Q1
SELECT c.customer_name, SUM(p.unit_price * oi.quantity) AS total_value
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
WHERE c.customer_city = 'Mumbai'
GROUP BY c.customer_name;

--Q2
SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 3;

-- Q3
SELECT s.sales_rep_name, COUNT(DISTINCT o.customer_id) AS customers_handled
FROM Sales_Reps s
JOIN Orders o ON s.sales_rep_id = o.sales_rep_id
GROUP BY s.sales_rep_name;

-- Q4
SELECT o.order_id, SUM(p.unit_price * oi.quantity) AS total_value
FROM Orders o
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
GROUP BY o.order_id
HAVING total_value > 10000
ORDER BY total_value DESC;

-- Q5
SELECT p.product_name
FROM Products p
LEFT JOIN Order_Items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;
