# pages/1_Analyze_Sentiment.py

import streamlit as st
from src.backend.model_loader import load_sentiment_model
from src.backend.sentiment_classifier import classify_sentiment
from src.config.settings import MODEL_OPTIONS, NEUTRAL_THRESHOLD
import datetime # Import datetime for timestamp
from styles import apply_custom_styles

st.set_page_config(page_title="Analyze Sentiment", layout="centered")

st.title("📝 Enter Text for Sentiment Analysis")
st.markdown("""
Type or paste your text below to get its sentiment analyzed.
You can also choose from a variety of pre-trained models.
""")

# Ensure analysis_history exists in session state
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

# Model Selection Dropdown
selected_model_name = st.selectbox(
    "Choose a Sentiment Model:",
    list(MODEL_OPTIONS.keys())
)
current_model_id = MODEL_OPTIONS[selected_model_name]

# Load the model and related components based on selection
tokenizer, model, id2label, label2id, device = load_sentiment_model(current_model_id)

#st.info(f"**Neutrality Threshold:** A text is classified as 'Neutral' if the absolute difference between its positive and negative probabilities is less than `{NEUTRAL_THRESHOLD}` (for 2-class models).")

# Input text area
# Initialize main_text_area in session_state if it doesn't exist
if 'main_text_area' not in st.session_state:
    st.session_state.main_text_area = ""

user_input = st.text_area(
    "Enter text for sentiment analysis:",
    value=st.session_state.main_text_area, # Explicitly link to session state
    height=150,
    placeholder="Type your sentence here...",
    key="main_text_area" # Keep the key
)

# --- Function to handle example selection ---
def select_example_callback():
    """
    Callback function when an example is selected from the dropdown.
    Sets the main text area and then clears the example selector.
    """
    if st.session_state.example_selector_value:
        st.session_state.main_text_area = st.session_state.example_selector_value
        # Reset the example selector to its default (empty string)
        st.session_state.example_selector_value = ""
        # Rerun is handled by on_change, but explicitly setting state is fine.

st.markdown("### Quick Examples:")
example_texts = [
    "This is an amazing product, I absolutely love it!",
    "I'm so frustrated with the slow service.",
    "The movie was okay, not great, not terrible.",
    "What a truly delightful experience!",
    "I hate this, it's a disaster.",
    "The weather is neither good nor bad today."
]
st.selectbox(
    "Or choose an example:",
    [""] + example_texts,
    key="example_selector_value",
    on_change=select_example_callback
)

# --- Callback for Clear Input Button ---
def clear_input_callback():
    st.session_state.main_text_area = ""
    st.session_state.example_selector_value = "" # Also clear example selection

col1, col2 = st.columns(2)

with col1:
    if st.button("Analyze Sentiment", use_container_width=True):
        if user_input:
            if model is None or tokenizer is None:
                st.error("Model is not loaded. Please check the console/terminal for loading errors.")
            else:
                with st.spinner("Analyzing sentiment..."):
                    sentiment, confidence, raw_scores = classify_sentiment(
                        user_input, tokenizer, model, id2label, label2id, device
                    )

                # Store current result for display on the next page
                st.session_state.current_analysis_result = {
                    "text": user_input,
                    "sentiment": sentiment,
                    "confidence": confidence,
                    "raw_scores": raw_scores,
                    "model_used": selected_model_name,
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                # Add to history
                st.session_state.analysis_history.append(st.session_state.current_analysis_result)

                st.success("Analysis complete! Redirecting to results...")
                st.switch_page("pages/2_Sentiment_Results.py") # Navigate to the hidden results page
        else:
            st.warning("Please enter some text to analyze.")

with col2:
    # Use the callback for the Clear Input button
    if st.button("Clear Input", on_click=clear_input_callback, use_container_width=True):
        pass # The action is handled by the callback, no need for code here

st.markdown("---")
st.caption("2025 © Advanced Sentiment Analysis App")
apply_custom_styles()