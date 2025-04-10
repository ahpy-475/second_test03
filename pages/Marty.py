import streamlit as st
import os
import google.generativeai as genai
st.title("Chat with Marty!")

key1 = st.secrets[key]

#client = genai.Client(api_key = key)
model = genai.GenerativeModel(key1)
response = model.generate_content("Write a poem about how learning web development is fun!")
st.write(response.text)

st.chat_input("Hey Transit Managers/Users! Ask Marty anything about MARTA")

st.chat_message()
