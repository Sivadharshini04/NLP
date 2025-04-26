!pip install textblob

from textblob import TextBlob

sentences = [
    "I love learning Conversational Systems!",
    "This is a terrible soup. I don't like it at all.",
    "The weather today is quite pleasant.",
    "I have mixed feelings about the new policy.",
    "I am sure it will be alright."
]


for sentence in sentences:
    blob = TextBlob(sentence)
    sentiment_score = blob.sentiment.polarity
    sentiment = 'positive' if sentiment_score > 0 else 'negative' if sentiment_score < 0 else 'neutral'

    print(f"Sentence: '{sentence}'")
    print(f"Sentiment Score: {sentiment_score:.2f}, Sentiment: {sentiment}\n")
