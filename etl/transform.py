def transform_sales_data(df):
    print("Starting transformation")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df["quantity"] = df["quantity"].fillna(1)

    # Convert date
    df["order_date"] = df["order_date"].astype("datetime64[ns]")

    # Create derived column
    df["total_amount"] = df["quantity"] * df["price"]

    print("Transformation completed")
    return df
