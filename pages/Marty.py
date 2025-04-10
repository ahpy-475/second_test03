import streamlit as st
import google.generativeai as genai
import os

st.title("Chat with Marty!")
key = st.secrets["key"]
genai.configure(api_key=key)

#client = genai.Client(api_key = key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a poem about how learning web development is fun!")
st.write(response.text)

prompt = st.chat_input("Hey Transit Managers/Users! Ask Marty anything about MARTA")
if prompt:
  #code for answering a question
  response = model.generate_content(prompt)
  st.write(response.text)

#st.chat_message()
