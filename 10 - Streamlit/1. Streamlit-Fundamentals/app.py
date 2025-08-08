import streamlit as st
import requests

# Title of the app
st.title("Chat with Gemma 2B (via Ollama)")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
user_input = st.chat_input("Ask something...")

# On submit
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display response while it's streaming
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Send request to Ollama API
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": user_input,
                "stream": True
            },
            stream=True,
        )

        # Stream response
        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8").replace("data: ", "")
                try:
                    token = eval(data).get("response", "")
                    full_response += token
                    message_placeholder.markdown(full_response + "▌")
                except Exception:
                    continue

        message_placeholder.markdown(full_response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})
