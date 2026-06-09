import pandas as pd
import numpy as np

df = pd.read_csv("online_retail_II.csv")
df.columns = df.columns.str.strip()

print("Columns found:")
print(df.columns.tolist())

rename_map = {
    'Invoice': 'InvoiceNo',
    'Customer ID': 'CustomerID',
    'Price': 'UnitPrice'
}

df.rename(columns=rename_map, inplace=True)
if 'InvoiceDate' not in df.columns:
    raise ValueError(
        f"InvoiceDate column not found.\nAvailable columns: {df.columns.tolist()}"
    )

df['InvoiceDate'] = pd.to_datetime(
    df['InvoiceDate'],
    dayfirst=True,
    errors='coerce'
)

df.dropna(subset=['InvoiceDate', 'CustomerID'], inplace=True)
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Revenue
df['Revenue'] = df['Quantity'] * df['UnitPrice']

df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
df['Hour'] = df['InvoiceDate'].dt.hour

first_purchase = df.groupby('CustomerID')['InvoiceMonth'].min()
df['CohortMonth'] = df['CustomerID'].map(first_purchase)

df['InvoiceMonth_int'] = (
    df['InvoiceMonth'].dt.year * 12 +
    df['InvoiceMonth'].dt.month
)

df['CohortMonth_int'] = (
    df['CohortMonth'].dt.year * 12 +
    df['CohortMonth'].dt.month
)

df['CohortAge'] = (
    df['InvoiceMonth_int'] -
    df['CohortMonth_int']
)

retention = (
    df.groupby(['CohortMonth', 'CohortAge'])['CustomerID']
    .nunique()
    .reset_index()
)
retention_matrix = retention.pivot(
    index='CohortMonth',
    columns='CohortAge',
    values='CustomerID'
)

retention_rate = (
    retention_matrix.divide(retention_matrix[0], axis=0) * 100
)
retention_rate.to_csv('retention_matrix.csv')
# Customer LTV
customer_revenue = df.groupby('CustomerID')['Revenue'].sum()
ltv_vals = customer_revenue.values
# KPIs
total_revenue = df['Revenue'].sum()
avg_order_value = df.groupby('InvoiceNo')['Revenue'].sum().mean()
peak_hour = df.groupby('Hour')['Revenue'].sum().idxmax()
top_country = df.groupby('Country')['Revenue'].sum().idxmax()
top_products = (
    df.groupby('Description')['Revenue']
    .sum()
    .nlargest(10)
)
top_customers = (
    df.groupby('CustomerID')['Revenue']
    .sum()
    .nlargest(10)
)

sorted_rev = customer_revenue.sort_values(ascending=False)
cum_pct = sorted_rev.cumsum() / sorted_rev.sum() * 100
customers_80 = (cum_pct <= 80).sum()

rev_vals = df['Revenue'].values
outliers = (
    rev_vals >
    rev_vals.mean() + 3 * rev_vals.std()
).sum()

df.to_csv('cleaned_data.csv', index=False)

if retention_rate.shape[1] > 1:
    highest_retention = retention_rate.iloc[:, 1].max()
else:
    highest_retention = 0

report = f"""
================================================================
E-COMMERCE CUSTOMER INTELLIGENCE REPORT
================================================================

Transactions: {len(df):,}
Customers: {df['CustomerID'].nunique():,}
Countries: {df['Country'].nunique():,}

Total Revenue: ${total_revenue:,.2f}
Average Order Value: ${avg_order_value:,.2f}

Median LTV: ${np.median(ltv_vals):.2f}
VIP Threshold (Top 10%): ${np.percentile(ltv_vals, 90):.2f}

Highest Month-1 Retention: {highest_retention:.2f}%
Peak Sales Hour: {peak_hour}:00
Top Country: {top_country}

Transactions > 3 Std Dev: {outliers}
Customers Driving 80% Revenue: {customers_80}

Top 10 Products:
{top_products.to_string()}

Top 10 Customers:
{top_customers.to_string()}
================================================================
"""

print(report)

with open('business_report.txt', 'w', encoding='utf-8') as f:
    f.write(report)

print("\nFiles saved:")
print(" - cleaned_data.csv")
print(" - retention_matrix.csv")
print(" - business_report.txt")
print("Project completed successfully!")