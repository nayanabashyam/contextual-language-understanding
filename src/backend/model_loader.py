# src/backend/model_loader.py

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

@st.cache_resource
def load_sentiment_model(model_name_id: str):
    """
    Loads the pre-trained sentiment analysis model and tokenizer based on the Hugging Face model ID.
    Caches the loaded resources to improve performance on subsequent runs.
    """
    try:
        # Load the tokenizer for processing text
        tokenizer = AutoTokenizer.from_pretrained(model_name_id)
        # Load the pre-trained model for sequence classification
        model = AutoModelForSequenceClassification.from_pretrained(model_name_id)

        # Retrieve the label mappings from the model's configuration
        # This is important because different models might have different label orders or names
        id2label = model.config.id2label
        label2id = model.config.label2id
        st.write(f"Model's specific label mapping: {id2label}") # Inform the user about the mapping

        # Determine the device to run the model on (GPU if available, otherwise CPU)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device) # Move the model to the determined device
        model.eval() # Set the model to evaluation mode (disables dropout, etc.)

        # st.success(f"Model '{model_name_id}' loaded successfully on {device}!")
        return tokenizer, model, id2label, label2id, device
    except Exception as e:
        # Display an error message if model loading fails
        st.error(f"Error loading model '{model_name_id}': {e}. Please check the model name and your internet connection.")
        return None, None, None, None, None