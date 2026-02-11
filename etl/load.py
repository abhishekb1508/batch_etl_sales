import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "sales_db",
    "user": "postgres",
    "password": "postgres"
}

def load_raw_data(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO sales_raw
            (order_id, order_date, customer_id, product_id,
             product_name, category, quantity, price)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            tuple(row.astype(str))
        )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Raw data loaded into sales_raw")


def load_processed_data(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO sales_processed
            (order_id, order_date, customer_id, product_id,
             product_name, category, quantity, price, total_amount)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (order_id) DO NOTHING
            """,
            tuple(row)
        )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Processed data loaded into sales_processed")
