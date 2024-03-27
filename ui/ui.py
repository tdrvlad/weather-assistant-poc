import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_PORT = os.getenv('API_PORT')
API_URL = f"http://localhost:{API_PORT}/chat"

st.title("Weather Assistant ⛅ ⛈ 🌧")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_message := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.markdown(user_message)
        data = {
            "user_message": user_message,
            "session_id": st.session_state.get("session_id", None)
        }

        try:
            response = requests.post(API_URL, json=data)
            response_data = response.json()
        except Exception as e:
            st.error(f"Failed to send message: {e}")

        response_message = response_data['response_message']
        session_id = response_data['session_id']

        st.session_state.messages.append({"role": "assistant", "content": response_message})
        st.session_state["session_id"] = session_id

    with st.chat_message("assistant"):
        st.write(response_data['response_message'])
