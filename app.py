import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Load pre-trained vectorizer and model
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: Missing 'vectorizer.pkl' or 'model.pkl'. Make sure both files are in the project directory.")
    st.stop()

# Initialize PorterStemmer
ps = PorterStemmer()

# Streamlit App Title
st.title("📩 Email/SMS Spam Classifier")


# Text Preprocessing Function
def transform_text(text):
    text = text.lower()
    text = "".join([char if char.isalnum() else " " for char in text])  # Remove punctuation
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stopwords.words('english')]  # Remove stopwords & stem words
    return " ".join(words)


# User Input
input_sms = st.text_area("Enter the message to classify")

# Prediction Button
if st.button('Predict'):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        # Preprocess input
        transformed_sms = transform_text(input_sms)

        # Vectorize input
        try:
            vector_input = tfidf.transform([transformed_sms])
        except ValueError as e:
            st.error("Vectorization error: Ensure 'vectorizer.pkl' matches the training data.")
            st.stop()

        # Predict
        result = model.predict(vector_input)[0]

        # Display Result
        if result == 1:
            st.header("🚨 Spam")
        else:
            st.header("✅ Not Spam")
