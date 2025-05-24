# analysis.py
# This script performs basic analysis on the cleaned dataset and prints insights.

import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_sales.csv')

# Show general summary statistics
print("\n Summary Statistics:\n")
print(df.describe())

# Group by product category to see total sales
cat_sales = df.groupby('Product Category')['Total Price'].sum().sort_values(ascending=False)

# Print category-wise total sales
print("\n Category-wise Sales:\n")
print(cat_sales)
