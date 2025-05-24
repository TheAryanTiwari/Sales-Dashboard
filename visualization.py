import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned_sales.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')

# Monthly sales trend
monthly_sales = df.groupby('Month')['Total Price'].sum()
monthly_sales.plot(kind='line', marker='o', figsize=(10, 5), title='Monthly Sales Trend')
plt.ylabel("Total Sales")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# Category-wise sales pie chart
cat_sales = df.groupby('Product Category')['Total Price'].sum()
cat_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig("category_sales_pie.png")
plt.show()
