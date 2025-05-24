import pandas as pd

df = pd.read_csv('data/larger_sales_dataset.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df = df[df['Order Status'] == 'Completed']
df['Month'] = df['Order Date'].dt.to_period('M')

df.to_csv('data/cleaned_sales.csv', index=False)
print(" Cleaned data saved to cleaned_sales.csv")