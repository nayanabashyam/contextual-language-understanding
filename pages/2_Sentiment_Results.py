# pages/_2_Sentiment_Results.py

import streamlit as st
from styles import apply_custom_styles

st.set_page_config(page_title="Current Analysis Results", layout="centered")

st.title("📊 Current Sentiment Analysis Results")

# Check if current_analysis_result exists in session state
if "current_analysis_result" in st.session_state and st.session_state.current_analysis_result:
    results = st.session_state.current_analysis_result

    st.subheader("Original Text:")
    st.info(f"**\" {results['text']} \"**")
    st.write(f"**Model Used:** {results.get('model_used', 'N/A')}")
    st.write(f"**Analysis Time:** {results.get('timestamp', 'N/A')}")

    st.markdown("---")
    st.subheader("Analysis Summary:")

    sentiment = results['sentiment']
    confidence = results['confidence']

    if sentiment == "Positive":
        st.success(f"**Overall Sentiment:** 🎉 {sentiment}")
    elif sentiment == "Negative":
        st.error(f"**Overall Sentiment:** 💔 {sentiment}")
    elif sentiment == "Neutral":
        st.warning(f"**Overall Sentiment:** ⚖️ {sentiment}")
    else:
        st.info(f"**Overall Sentiment:** ❓ {sentiment}")

    st.write(f"**Confidence:** {confidence:.2%}")

    st.write("---")
    st.subheader("Raw Probability Scores:")
    # Sort scores for consistent display
    sorted_scores = sorted(results['raw_scores'].items(), key=lambda item: item[0])
    for label, score in sorted_scores:
        st.metric(label.capitalize(), f"{score:.2%}")

    st.markdown("---")
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("Analyze Another Text", use_container_width=True):
            st.switch_page("pages/1_Analyze_Sentiment.py")
    with col_nav2:
        if st.button("View Analysis History", use_container_width=True):
            st.switch_page("pages/3_Analysis_History.py")

else:
    st.warning("No current analysis results found. Please go back to the 'Analyze Sentiment' page to input text.")
    if st.button("Go to Analyze Sentiment Page"):
        st.switch_page("pages/1_Analyze_Sentiment.py")

st.markdown("---")
st.caption("2025 © Advanced Sentiment Analysis App")
apply_custom_styles()