# Home.py

import streamlit as st
from styles import apply_custom_styles

st.set_page_config(page_title="Advanced Sentiment Analysis App", layout="centered")

st.title("Welcome to the Advanced Sentiment Analysis App 🗣️")
st.markdown("""
This application allows you to analyze the sentiment of any text you provide.
""")

# Button to navigate to the Analyze Sentiment page
if st.button("Get Started: Analyze Sentiment"):
    st.switch_page("pages/1_Analyze_Sentiment.py")

st.markdown("---")
st.caption("2025 © Advanced Sentiment Analysis App")
apply_custom_styles()