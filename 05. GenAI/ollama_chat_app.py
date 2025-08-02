import streamlit as st
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def stream_ollama_response(prompt, model="gemma:2b", temperature=0.7, max_tokens=300):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "temperature": temperature,
            "stream": True,
            "options": {
                "num_predict": max_tokens
            }
        },
        stream=True
    )
    for line in response.iter_lines():
        if line:
            yield json.loads(line.decode("utf-8")).get("response", "")

st.set_page_config(page_title="Ollama Chat", layout="wide")
st.title("Chat with Local LLM (Ollama)")

if "history" not in st.session_state:
    st.session_state.history = []

# Only available models
available_models = ["gemma:2b", "llama3"]

model = st.selectbox("Choose a model", available_models, index=0)
temperature = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.05)
max_tokens = st.slider("Max Tokens", 50, 1000, 300, step=50)

prompt = st.text_area("Enter your prompt")

if st.button("Submit") and prompt.strip():
    with st.spinner("Generating response..."):
        st.session_state.history.append(("You", prompt))
        response_text = ""
        response_area = st.empty()

        for chunk in stream_ollama_response(prompt, model, temperature, max_tokens):
            response_text += chunk
            response_area.markdown(f"**LLM:** {response_text}")

        st.session_state.history.append(("LLM", response_text))

# Show chat history (latest first)
for sender, message in reversed(st.session_state.history):
    st.markdown(f"**{sender}:** {message}")
