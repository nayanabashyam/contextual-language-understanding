# src/backend/sentiment_classifier.py

import torch
import numpy as np
from scipy.special import softmax
# Import NEUTRAL_THRESHOLD from the settings file
from src.config.settings import NEUTRAL_THRESHOLD

def classify_sentiment(text: str, current_tokenizer, current_model, current_id2label, current_label2id, current_device):
    """
    Classifies the sentiment of a given text using the loaded Transformer model.

    Args:
        text (str): The input text to classify.
        current_tokenizer: The tokenizer object loaded for the current model.
        current_model: The pre-trained model object loaded for sentiment analysis.
        current_id2label (dict): Mapping from label ID to label name from the model's config.
        current_label2id (dict): Mapping from label name to label ID from the model's config.
        current_device: The PyTorch device ('cpu' or 'cuda') the model is running on.

    Returns:
        tuple: A tuple containing the predicted label (str), confidence score (float),
               and a dictionary of all raw probability scores.
    """
    if current_model is None or current_tokenizer is None:
        # Return default error values if model or tokenizer isn't loaded
        return "Error", 0.0, {'NEGATIVE': 0.0, 'POSITIVE': 0.0, 'NEUTRAL': 0.0}

    if not text.strip(): # Handle empty input gracefully
        return "Neutral", 0.0, {'NEGATIVE': 0.0, 'POSITIVE': 0.0, 'NEUTRAL': 0.0}

    # Tokenize the input text and move to the appropriate device
    inputs = current_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {k: v.to(current_device) for k, v in inputs.items()}

    with torch.no_grad(): # Disable gradient calculation for inference
        outputs = current_model(**inputs)

    logits = outputs.logits
    # Convert logits to probabilities using softmax
    probabilities = softmax(logits.cpu().numpy(), axis=1)[0]

    # --- Handle varying label mappings ---
    scores_dict = {}
    for i, label_name in current_id2label.items():
        # Map probabilities to their corresponding label names (e.g., 'LABEL_0', 'NEGATIVE', 'positive')
        scores_dict[label_name.upper()] = probabilities[i]

    # Get probabilities for common sentiment labels, defaulting to 0.0 if not present
    neg_prob = scores_dict.get('NEGATIVE', 0.0)
    pos_prob = scores_dict.get('POSITIVE', 0.0)
    neutral_prob = scores_dict.get('NEUTRAL', 0.0) # For models that explicitly predict 'NEUTRAL'

    all_scores = scores_dict # Keep all scores as reported by the model

    predicted_label = ""
    confidence_score = 0.0

    # Determine sentiment based on probabilities and the NEUTRAL_THRESHOLD
    if abs(pos_prob - neg_prob) < NEUTRAL_THRESHOLD and 'NEUTRAL' not in all_scores:
        # If the difference between positive and negative is small, infer as Neutral
        predicted_label = "Neutral"
        confidence_score = max(pos_prob, neg_prob) # Confidence in inferred neutral
    elif 'NEUTRAL' in all_scores and neutral_prob > pos_prob and neutral_prob > neg_prob:
        # If the model explicitly predicts Neutral and it's the highest, use it
        predicted_label = "Neutral"
        confidence_score = neutral_prob
    elif pos_prob > neg_prob:
        predicted_label = "Positive"
        confidence_score = pos_prob
    else: # neg_prob >= pos_prob
        predicted_label = "Negative"
        confidence_score = neg_prob

    return predicted_label, confidence_score, all_scores