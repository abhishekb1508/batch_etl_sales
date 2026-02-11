import pandas as pd
from transform import transform_sales_data
from validation import validate_sales_data

df = pd.read_csv("data/sales_raw.csv")
df = transform_sales_data(df)
validate_sales_data(df)

print("🎉 Transform + Validation completed successfully")
