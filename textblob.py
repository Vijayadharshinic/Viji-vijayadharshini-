from textblob import TextBlob

def detect_harsh_talk(text):
    """
    Function to detect negative sentiment in text as a proxy for harsh talk.
    Note: This is a very simplistic approach and not reliable for nuanced detection.
    """
    testimonial = TextBlob(text)
    sentiment = testimonial.sentiment.polarity
    if sentiment < -0.3:  # Arbitrary threshold for simplicity
        return "Potential harsh talk detected."
    else:
        return "No harsh talk detected."

# Example texts
texts = [
    "I think you could have done better.",
    "That was a terrible idea!",
    "I love how you handled that situation."
]

for text in texts:
    print(f"Text: {text}\nResult: {detect_harsh_talk(text)}\n")
