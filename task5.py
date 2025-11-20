import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales.csv")   # update with your file name
print(df.head())

# Basic info
print("Shape:", df.shape)
print("Columns:", df.columns)

# Group by category example
sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)

# Plot chart
sales_by_category.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
