import streamlit as st
import google.generativeai as genai
import os
API_URL = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"

def fetch_marta_data():
    info = requests.get(API_URL)
    data = info.json()
    return data


st.title("Chat with Marty!")
key = st.secrets["key"]
genai.configure(api_key=key)

#client = genai.Client(api_key = key)
model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Write a poem about how learning web development is fun!")
#st.write(response.text)

prompt = st.chat_input("Hey Transit Managers/Users! Ask Marty anything about MARTA")
if prompt:
  #code for answering a question
  response = model.generate_content(prompt)
  st.write(response.text)

#st.chat_message()
