import pandas as pd

# Load dataset
data = pd.read_csv("bestsellers.csv")

# Show first rows
print(data.head())

# Check missing values
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

# Show columns
print(data.columns)

# Calculate average price
avg_price = data["Price"].mean()
print("Average Price:", avg_price)

# Find max rating
max_rating = data["User Rating"].max()
print("Max Rating:", max_rating)

# Find min price
min_price = data["Price"].min()
print("Min Price:", min_price)

# Count categories
count = data["Genre"].value_counts()
print(count)

# Show top 5 expensive books
top = data.sort_values(by="Price", ascending=False)
print(top.head())

print("Done")