import streamlit as st
import os
import google.generativeai as genai
st.title("Hey this is the page where you will be able to talk with Marty!")

#client = genai.Client(api_key = key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a poem about how learning web development is fun!")
st.write(response.text)
