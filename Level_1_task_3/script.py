import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

# Drop rows where latitude or longitude is missing
df = df.dropna(subset=['Latitude', 'Longitude'])

# Scatter plot of restaurant locations
plt.figure(figsize=(10,6))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.3, s=10, color='purple')
plt.title('Restaurant Locations (Longitude vs Latitude)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

# Number of restaurants per country
print("\nTop 10 Countries with Most Restaurants:\n")
print(df['Country Code'].value_counts().head(10))

# Correlation between latitude, longitude, and aggregate rating
print("\nCorrelation between Location and Rating:\n")
print(df[['Latitude', 'Longitude', 'Aggregate rating']].corr())
