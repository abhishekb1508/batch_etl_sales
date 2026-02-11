-- Total revenue
SELECT SUM(total_amount) AS total_revenue
FROM sales_processed;

-- Revenue by category
SELECT category, SUM(total_amount) AS revenue
FROM sales_processed
GROUP BY category
ORDER BY revenue DESC;

-- Top-selling products
SELECT product_name, SUM(quantity) AS units_sold
FROM sales_processed
GROUP BY product_name
ORDER BY units_sold DESC;

-- Daily revenue trend
SELECT order_date, SUM(total_amount) AS daily_revenue
FROM sales_processed
GROUP BY order_date
ORDER BY order_date;
