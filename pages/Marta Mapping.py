import streamlit as st
st.title("Hey this is the API Webpage where we are showing the data of the trains!")

import streamlit as st
import requests

# MARTA API URL (Replace with actual API if needed)
API_URL = "https://api.itsmarta.com/RealtimeTrainPositions"

# Function to fetch train data
def fetch_marta_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return []

# Fetch train data
train_data = fetch_marta_data()

# Get unique stations from API data
stations = sorted(set(train["STATION"] for train in train_data))

# Streamlit UI
st.set_page_config(page_title="MARTA Pokedex 🚆", layout="wide")

st.title("🚆 MARTA Train Pokedex")
st.write("Select your station to see which trains are arriving **on time!**")

# User selects a station
selected_station = st.selectbox("📍 Choose Your Station:", ["Choose a station"] + stations)

# Display train info if a station is selected
if selected_station and selected_station != "Choose a station":
    st.subheader(f"🚉 On-Time Trains at **{selected_station}**")

    # Filter trains for the selected station
    trains_at_station = [train for train in train_data if train["STATION"] == selected_station]

    # Filter only "On Time" trains (Modify based on actual API data)
    on_time_trains = [train for train in trains_at_station if train["STATUS"] == "On Time"]

    if on_time_trains:
        # Create a card-like display using Streamlit columns
        cols = st.columns(2)  # Two columns for displaying train cards

        for idx, train in enumerate(on_time_trains):
            arrival_time = round(int(train["SECONDS_TO_ARRIVAL"]) / 60)  # Convert seconds to minutes
            
            with cols[idx % 2]:  # Alternate between columns
                st.markdown(
                    f"""
                    <div style="background-color:#1E88E5; color:white; padding:15px; border-radius:10px; text-align:center; margin-bottom:10px;">
                        <h3>{train['LINE']} Line</h3>
                        <p>🚊 <b>Arriving in {arrival_time} min</b></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.warning("No on-time trains at this station.")

import matplotlib.pyplot as plt
