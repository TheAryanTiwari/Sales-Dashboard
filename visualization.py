# visualizations.py
# This script generates and saves visualizations for the cleaned sales data.

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_sales.csv')

# Convert 'Order Date' to datetime again (in case it loaded as string)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create a 'Month' column again (safety)
df['Month'] = df['Order Date'].dt.to_period('M')

#  Line Chart: Monthly Sales Trend
monthly_sales = df.groupby('Month')['Total Price'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='skyblue')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.show()

#  Pie Chart: Category-wise Sales
cat_sales = df.groupby('Product Category')['Total Price'].sum()
cat_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig('category_sales_pie.png')
plt.show()
