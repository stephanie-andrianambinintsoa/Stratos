import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# File path to your CSV file
file_path = 'C:\\Users\\arman\\Downloads\\Project Cleaning and Formatting of Phone Numbers - Customers_books_purchases.csv'

# Load the data
data = pd.read_csv(file_path)

# Display basic information about the data
print("Data Information:")
print(data.info())

print("\nFirst few rows of the data:")
print(data.head())

# Convert PurchaseDate to datetime
data['PurchaseDate'] = pd.to_datetime(data['PurchaseDate'])

# Sales over time
plt.figure(figsize=(10, 6))
sales_over_time = data.groupby('PurchaseDate')['PurchaseAmount'].sum().reset_index()
plt.plot(sales_over_time['PurchaseDate'], sales_over_time['PurchaseAmount'], marker='o', linestyle='-', color='b')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_over_time.png')
plt.show()

# Pair Plot for Outlier Detection
plt.figure(figsize=(12, 10))
sns.pairplot(data[['CustomerID', 'PurchaseAmount']], diag_kind='kde', hue='PurchaseAmount', palette='viridis')
plt.title('Pair Plot for Outlier Detection')
plt.tight_layout()
plt.savefig('pair_plot_outliers.png')
plt.show()

# Histogram of Purchase Amounts with Rainbow Bars
plt.figure(figsize=(10, 6))
purchase_amounts = data['PurchaseAmount']
num_bins = 10
bin_edges = np.linspace(purchase_amounts.min(), purchase_amounts.max(), num_bins + 1)
colors = plt.cm.rainbow(np.linspace(0, 1, num_bins))

# Create histogram with individual bar colors
for i in range(num_bins):
    bin_data = purchase_amounts[(purchase_amounts >= bin_edges[i]) & (purchase_amounts < bin_edges[i + 1])]
    plt.hist(bin_data, bins=[bin_edges[i], bin_edges[i + 1]], color=colors[i], edgecolor='black', alpha=0.7, label=f'Bin {i + 1}' if i == 0 else "")

plt.title('Histogram of Purchase Amounts')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('purchase_amount_histogram.png')
plt.show()

# Box Plot of Purchase Amounts
plt.figure(figsize=(10, 6))
sns.boxplot(x='PurchaseAmount', data=data, color='lightblue')
plt.title('Box Plot of Purchase Amounts')
plt.xlabel('Purchase Amount')
plt.grid(True)
plt.tight_layout()
plt.savefig('purchase_amount_box_plot.png')
plt.show()
