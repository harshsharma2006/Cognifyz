import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Step 1: Basic info
print("💰 Cost for 2 People (first 5 rows):")
print(df[['Restaurant Name', 'Average Cost for two']].head())

# Step 2: Top 10 expensive restaurants
print("\n💸 Top 10 Most Expensive Restaurants:")
expensive = df[['Restaurant Name', 'City', 'Average Cost for two']].sort_values(by='Average Cost for two', ascending=False).head(10)
print(expensive)

# Step 3: Average cost by city
print("\n🏙️ Average Cost for Two by City (Top 5):")
print(df.groupby('City')['Average Cost for two'].mean().sort_values(ascending=False).head(5))

# Step 4: Scatter Plot - Votes vs Rating
plt.figure(figsize=(8,5))
plt.scatter(df['Aggregate rating'], df['Votes'], alpha=0.4, color='green')
plt.title("Votes vs Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Votes")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Affordable High Rated Places
print("\n🌟 High Rated & Low Cost Restaurants (Rating > 4.0 & Cost < 400):")
filtered = df[(df['Aggregate rating'] > 4.0) & (df['Average Cost for two'] < 400)]
print(filtered[['Restaurant Name', 'City', 'Aggregate rating', 'Average Cost for two']].head(10))
