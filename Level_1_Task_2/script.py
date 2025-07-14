import pandas as pd

df = pd.read_csv("Dataset.csv")

print("Descriptive Statistics:\n")
print(df.describe())

print("\nNumber of unique Country Codes:", df['Country Code'].nunique())
print("Number of unique Cities:", df['City'].nunique())
print("Number of unique Cuisines:", df['Cuisines'].nunique())

print("\nTop 10 Most Common Cuisines:\n")
print(df['Cuisines'].value_counts().head(10))

print("\nTop 10 Cities with the Most Restaurants:\n")
print(df['City'].value_counts().head(10))
