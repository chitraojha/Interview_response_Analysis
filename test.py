import spacy
from textblob import TextBlob

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_sentiment(response):
    blob = TextBlob(response)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def extract_key_phrases(response):
    doc = nlp(response)
    key_phrases = [chunk.text for chunk in doc.noun_chunks]
    return key_phrases

def assess_quality(sentiment, key_phrases):
    # Simple assessment based on sentiment and number of key phrases
    if sentiment == "Positive" and len(key_phrases) > 3:
        return "High"
    elif sentiment == "Neutral" and len(key_phrases) > 2:
        return "Medium"
    else:
        return "Low"

# Read responses from file
with open("interview_responses.txt", "r") as f:
    responses = [line.strip() for line in f.readlines()]

# Analyze each response
for i, response in enumerate(responses, start=1):
    sentiment = analyze_sentiment(response)
    key_phrases = extract_key_phrases(response)
    quality = assess_quality(sentiment, key_phrases)
    
    print(f"Response {i}:")
    print(f"Sentiment: {sentiment}")
    print(f"Key Phrases: {key_phrases}")
    print(f"Overall Quality: {quality}")
    print("-" * 40)