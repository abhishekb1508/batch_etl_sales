def validate_sales_data(df):
    print("Starting data validation")

    if df["order_id"].isnull().any():
        raise ValueError("❌ Validation failed: order_id contains null values")

    if (df["quantity"] <= 0).any():
        raise ValueError("❌ Validation failed: quantity must be greater than 0")

    if (df["price"] <= 0).any():
        raise ValueError("❌ Validation failed: price must be greater than 0")

    print("✅ Data validation passed")
