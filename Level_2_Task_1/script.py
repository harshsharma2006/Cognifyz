import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")
df['Cuisines'] = df['Cuisines'].fillna("Unknown")

print(df.describe())
print(df['City'].value_counts().head(5))
print(df['Cuisines'].value_counts().head(5))
print(df['Country Code'].value_counts().head(5))

df['City'].value_counts().head(5).plot(kind='bar', color='orange')
plt.title("Top 5 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.grid(True)
plt.tight_layout()
plt.show()
