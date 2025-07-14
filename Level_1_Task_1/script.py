import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

print("Shape of the dataset:", df.shape)
print("\nColumn Names:\n", df.columns.tolist())

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nData Types:\n")
print(df.dtypes)

df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

print("\nDistribution of 'Aggregate rating':\n")
print(df['Aggregate rating'].value_counts().sort_index())

plt.figure(figsize=(8,5))
df['Aggregate rating'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Number of Restaurants')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
