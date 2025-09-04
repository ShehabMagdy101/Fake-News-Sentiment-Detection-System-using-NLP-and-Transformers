import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model
model_path = '../models/distilbert-fake-news'

@st.cache_resource  # cache so it doesn’t reload every time
def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

model, tokenizer = load_model()

st.header(":red[Fake] News Detector", divider=True)

user_input = st.text_area("Enter a news article:")

if st.button("Predict"):
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=-1).item()
    labels = ["Fake", "Real"]
    if labels[prediction] == 'Fake':
        st.write("Prediction:", ":red[Fake]")
    else:
        st.write("Prediction:", ":green[Real]")

