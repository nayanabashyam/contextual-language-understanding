# src/config/settings.py

# Define a dictionary of models the user can choose from in the Streamlit app.
# Key: Display name shown in the app's dropdown.
# Value: Corresponding Hugging Face model ID (used for loading).
MODEL_OPTIONS = {
    "DistilBERT (Negative,Positive)": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    "RoBERTa (Negative,Neutral,Positive)": "cardiffnlp/twitter-roberta-base-sentiment-latest",
    # You can add more models here, for example:
    # "BERT (Multilingual 5-star)": "nlptown/bert-base-multilingual-uncased-sentiment",
    # "Fine-tuned BERT (Financial News)": "ProsusAI/finbert"
}

# The threshold for classifying a text as 'Neutral'.
# If the absolute difference between positive and negative probabilities is below this value,
# and the model doesn't explicitly have a 'Neutral' class, it's inferred as Neutral.
# Adjust this value (0.0 to 1.0) to make the app more or less sensitive to neutrality.
NEUTRAL_THRESHOLD = 0.15