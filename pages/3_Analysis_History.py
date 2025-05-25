# pages/3_Analysis_History.py

import streamlit as st
from styles import apply_custom_styles

st.set_page_config(page_title="Analysis History", layout="centered")

st.title("📜 Your Analysis History")
st.markdown("""
Here you can review all the sentiment analysis results from your current session.
""")

if 'analysis_history' in st.session_state and st.session_state.analysis_history:
    # Display in reverse chronological order (most recent first)
    for i, result in enumerate(reversed(st.session_state.analysis_history)):
        st.markdown(f"### Analysis #{len(st.session_state.analysis_history) - i} (Time: {result.get('timestamp', 'N/A')})")
        st.markdown(f"**Text:** _{result['text']}_")
        
        sentiment = result['sentiment']
        if sentiment == "Positive":
            st.success(f"**Sentiment:** 🎉 {sentiment} | **Confidence:** {result['confidence']:.2%}")
        elif sentiment == "Negative":
            st.error(f"**Sentiment:** 💔 {sentiment} | **Confidence:** {result['confidence']:.2%}")
        elif sentiment == "Neutral":
            st.warning(f"**Sentiment:** ⚖️ {sentiment} | **Confidence:** {result['confidence']:.2%}")
        else:
            st.info(f"**Sentiment:** ❓ {sentiment} | **Confidence:** {result['confidence']:.2%}")

        st.write(f"**Model Used:** {result.get('model_used', 'N/A')}")
        
        with st.expander("Show Raw Probabilities"):
            for label, score in sorted(result['raw_scores'].items(), key=lambda item: item[0]):
                st.markdown(f"- **{label.capitalize()}:** {score:.2%}")
        st.markdown("---")
    
    if st.button("Clear History", type="secondary"):
        st.session_state.analysis_history = []
        st.success("Analysis history cleared!")
        st.rerun() # Rerun to reflect the cleared history

else:
    st.info("No analysis history yet. Analyze some text to see it here!")

st.markdown("---")
if st.button("Go to Analyze Sentiment Page"):
    st.switch_page("pages/1_Analyze_Sentiment.py")

st.write("History is cleared when the browser tab is closed.")
st.markdown("---")
st.caption("2025 © Advanced Sentiment Analysis App")
apply_custom_styles()