import streamlit as st
import os
from google import genai
st.title("Hey this is the page where you will be able to talk with Marty!")

client = genai.Client(api_key = key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = client.model.generate_content("Make a plan on how to study for and intro to Python Course Final Exam")
print(response.text)
