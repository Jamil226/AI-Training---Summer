import streamlit as st
import torch
from transformers import pipeline

# Use the updated caching method
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

# Streamlit UI
st.title("GPT-2 Text Generator")
st.write("Type a prompt and click 'Generate' to see what the model writes!")

# User input
prompt = st.text_input("Enter your prompt", "Once upon a time")
max_len = st.slider("Max length", min_value=10, max_value=100, value=30, step=5)

# Generate text
if st.button("Generate"):
    with st.spinner("Generating..."):
        result = generator(prompt, max_length=max_len, num_return_sequences=1)
        generated_text = result[0]['generated_text']
        st.subheader("Generated Text")
        st.write(generated_text)
