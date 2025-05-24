import pandas as pd

df = pd.read_csv('data/cleaned_sales.csv')

print("\n Summary Statistics:\n", df.describe())

cat_sales = df.groupby('Product Category')['Total Price'].sum().sort_values(ascending=False)
print("\n Category-wise Sales:\n", cat_sales)
