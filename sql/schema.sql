CREATE TABLE IF NOT EXISTS sales_raw (
    order_id TEXT,
    order_date TEXT,
    customer_id TEXT,
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    quantity TEXT,
    price TEXT,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sales_processed (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    product_name VARCHAR(50),
    category VARCHAR(30),
    quantity INT,
    price NUMERIC,
    total_amount NUMERIC
);
