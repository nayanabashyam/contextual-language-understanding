# styles.py
import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
            /* Textarea */
            textarea, .stTextArea > div > div > textarea {
                border: 2px solid #A9A9A9 !important; /* grey */
                border-radius: 8px !important;
                padding: 8px !important;
            }

            /* Dropdown / Selectbox */
            .stSelectbox > div {
                border: 2px solid #A9A9A9 !important; /* grey */
                border-radius: 8px !important;
            }

            /* Buttons */
            button {
                border: 2px solid #A9A9A9 !important; /* grey */
                border-radius: 8px !important;
                background-color: #f9f9f9 !important;
                color: black !important;
            }

            button:hover {
                border-color: #808080 !important; /* darker grey on hover */
                background-color: #f0f0f0 !important;
            }
        </style>
    """, unsafe_allow_html=True)
