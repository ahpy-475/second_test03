import streamlit as st
import google.generativeai as genai
import os
API_URL = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"

def fetch_marta_data():
    info = requests.get(API_URL)
    data = info.json()
    return data


st.title("Manage with Marty!")
st.write("Marty will answer real-time questions backed by data")
key = st.secrets["key"]
genai.configure(api_key=key)

#client = genai.Client(api_key = key)
model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Write a poem about how learning web development is fun!")
#st.write(response.text)


st.header("If you are looking for information on WHERE a train is:")
train_query = st.write("Choose what train you are looking for:")
for i in len(train_query):
    if i.isDigit():
        number += i
num = int(number)

train_query = num

if data["TRAIN_ID"] == num:
    

st.header("If you are looking for information on HOW LONG until a train arrives at a location:")
loc_query = st.write("Pick what location you are trying to go to:")



prompt = st.chat_input("Hey Transit Managers! Ask Marty anything about MARTA")
if prompt:
  #code for answering a question
  response = model.generate_content(prompt)
  st.write(response.text)

#st.chat_message()
