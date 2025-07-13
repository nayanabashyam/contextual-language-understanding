# Contextual Language Understanding using NLPtransformers 

This is a Streamlit-powered web application for performing sentiment analysis using various pre-trained Hugging Face Transformer models.

## Project Structure

-   `Home.py`: The main entry point of the multi-page Streamlit application, serving as the welcome page.
-   `pages/`: Contains separate Python files for each page of the application.
    -   `1_Analyze_Sentiment.py`: The primary page where users input text, select a model, and initiate analysis.
    -   `_2_Sentiment_Results.py`: A **hidden page** (not shown in the sidebar) that displays the *current* sentiment analysis results. Navigation to this page happens automatically after analysis.
    -   `3_Analysis_History.py`: A page to view a list of all past analysis results from the current session.
-   `src/`: Contains the core logic, separated into backend and configuration.
    -   `src/backend/`: Logic related to model loading and sentiment classification.
        -   `model_loader.py`: Handles loading Transformer models and tokenizers.
        -   `sentiment_classifier.py`: Contains the core sentiment classification function.
    -   `src/config/`: Configuration settings for the application.
        -   `settings.py`: Defines model options, neutrality threshold, and other global settings.
    -   `src/frontend/`: (Currently a placeholder, would house reusable UI functions for complex UIs).
-   `requirements.txt`: Lists all Python dependencies.
-   `README.md`: This file.

## Setup and Installation

1.  **Clone the repository (or create files manually as shown):**
    ```bash
    git clone <your-repository-url> # If you're setting up a repo
    cd finalproj
    ```

2.  **Create a virtual environment (highly recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Activate your virtual environment** (if not already active):
    ```bash
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

2.  **Run the Streamlit application:**
    ```bash
    streamlit run Home.py
    ```

    This will open the application in your default web browser.

## Features

-   **Streamlined Navigation:** Dedicated "Home" page with a "Get Started" button.
-   **Clear Page Separation:** Input on "Analyze Sentiment" page, current result on a separate (hidden) page.
-   **Analysis History:** A new page to review all analyses performed during the current session.
-   **Model Selection:** Choose from different pre-trained Hugging Face sentiment models.
-   **Dynamic Input:** Analyze custom text or use provided examples.
-   **Detailed Results:** View predicted sentiment, confidence score, and raw probability scores.
-   **User-Friendly Input:** Example selection resets, and input can be cleared.

## Configuration

You can adjust the following settings in `src/config/settings.py`:

-   `MODEL_OPTIONS`: Add or remove Hugging Face model IDs to change the available models in the dropdown.
-   `NEUTRAL_THRESHOLD`: Modify the threshold used to classify text as 'Neutral' for 2-class models.

## Technologies Used

-   Python
-   Streamlit
-   Hugging Face Transformers
-   PyTorch
