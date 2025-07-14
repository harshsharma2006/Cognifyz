import pandas as pd

df = pd.read_csv("Dataset.csv")
df['Cuisines'] = df['Cuisines'].fillna("Unknown")

def recommend_by_cuisine(cuisine):
    result = df[df['Cuisines'].str.contains(cuisine, case=False, na=False)]
    return result[['Restaurant Name', 'City', 'Cuisines', 'Aggregate rating']].sort_values(by='Aggregate rating', ascending=False).head(10)

user_input = input("Enter a cuisine you like (e.g., Chinese, Italian, Indian): ")
print(f"\nTop Restaurants for {user_input} Cuisine:")
print(recommend_by_cuisine(user_input))

def recommend_top_in_city(city):
    result = df[df['City'].str.contains(city, case=False, na=False)]
    return result[['Restaurant Name', 'Cuisines', 'Aggregate rating']].sort_values(by='Aggregate rating', ascending=False).head(10)

user_city = input("\nEnter your city: ")
print(f"\nTop Restaurants in {user_city}:")
print(recommend_top_in_city(user_city))
