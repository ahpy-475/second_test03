import streamlit as st
import requests
import matplotlib.pyplot as plt

# ✅ Set page config at the very top
st.set_page_config(page_title="MARTA Pokedex 🚆", layout="wide")

# 🚆 MARTA API URL
API_URL = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"

# 🎯 Function to fetch train data
def fetch_marta_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raises an error for HTTP issues
        data = response.json()

        # ✅ Ensure data is a list of dictionaries
        if isinstance(data, list) and all(isinstance(train, dict) for train in data):
            return data
        else:
            st.error("Unexpected API response format.")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

# 📊 Fetch train data
