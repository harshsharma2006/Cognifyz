import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")
df = df[df['Aggregate rating'] > 0]

print(df['Aggregate rating'].value_counts().sort_index())

df['Aggregate rating'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("Rating Distribution of Restaurants")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.grid(True)
plt.tight_layout()
plt.show()

print(df.groupby('Has Online delivery')['Aggregate rating'].mean())
print(df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10))
