# clean_data.py
# This script loads the raw sales dataset, cleans it, and saves a cleaned version.

import pandas as pd

# Load the dataset
df = pd.read_csv('data/larger_sales_dataset.csv')

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Drop rows with missing values
df.dropna(inplace=True)

# Remove any duplicate rows
df.drop_duplicates(inplace=True)

# Filter only 'Completed' orders
df = df[df['Order Status'] == 'Completed']

# Create a new column for month-year (for trend analysis)
df['Month'] = df['Order Date'].dt.to_period('M')

# Save the cleaned dataset
df.to_csv('data/cleaned_sales.csv', index=False)

print(" Cleaned data saved to data/cleaned_sales.csv")
