import pandas as pd

df = pd.read_csv("Dataset.csv")
df = df[df['Aggregate rating'] != 0]

def classify_sentiment(rating):
    if rating >= 4.0:
        return "Positive"
    elif rating >= 3.0:
        return "Neutral"
    else:
        return "Negative"

df['Sentiment'] = df['Aggregate rating'].apply(classify_sentiment)

print(df[['Restaurant Name', 'Aggregate rating', 'Sentiment']].head())

sentiment_counts = df['Sentiment'].value_counts()

import matplotlib.pyplot as plt

sentiment_counts.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title("Sentiment Classification Based on Ratings")
plt.xlabel("Sentiment")
plt.ylabel("Number of Restaurants")
plt.grid(True)
plt.tight_layout()
plt.show()
