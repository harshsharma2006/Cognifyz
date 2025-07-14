import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")
df['Cuisines'] = df['Cuisines'].fillna("Unknown")
df = df[df['Aggregate rating'] > 0]

def sentiment(r):
    if r >= 4.0:
        return "Positive"
    elif r >= 3.0:
        return "Neutral"
    else:
        return "Negative"

df['Sentiment'] = df['Aggregate rating'].apply(sentiment)

top_cities = df['City'].value_counts().head(5)
sentiment_counts = df['Sentiment'].value_counts()
rating_dist = df['Aggregate rating'].value_counts().sort_index()

plt.figure(figsize=(16, 4))

plt.subplot(1, 3, 1)
top_cities.plot(kind='bar', color='skyblue')
plt.title("Top Cities")

plt.subplot(1, 3, 2)
sentiment_counts.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title("Sentiment Overview")

plt.subplot(1, 3, 3)
rating_dist.plot(kind='bar', color='purple')
plt.title("Rating Distribution")

plt.tight_layout()
plt.show()
