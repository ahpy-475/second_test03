import streamlit as st
import requests
#import matplotlib.pyplot as plt

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
train_data = fetch_marta_data()

# 🔍 Extract unique station names
stations = sorted(set(train.get("STATION", "Unknown") for train in train_data))

st.title(" MARTA Times")
st.write("Select your station to see which trains are arriving **next**")

selected_station = st.selectbox(" Choose Your Station:", ["Choose a station"] + stations)

if selected_station and selected_station != "Choose a station":
    st.subheader(f"Time until next train arrives at **{selected_station}:**")

    trains_at_station = [train for train in train_data if train.get("STATION") == selected_station]

    on_time_trains = [train for train in trains_at_station if train.get("STATUS") == "On Time"]

    if trains_at_station:
        cols = st.columns(2)  # Two-column layout

        for i, train in enumerate(on_time_trains):
            arrival_seconds = train.get("WAITING_SECONDS", "0")
            try:
                arrival_time = round(int(arrival_seconds) / 60)  # Convert seconds to minutes
            except ValueError:
                arrival_time = "N/A"  # Fallback if conversion fails
            
            with cols[idx % 2]:  # Alternate between columns
                st.markdown(
                    f"""
                    <div style="background-color:#1E88E5; color:white; padding:15px; border-radius:10px; text-align:center; margin-bottom:10px;">
                        <h3>{train.get('LINE', 'Unknown')} Line</h3>
                        <p>🚊 <b>Arriving in {arrival_time} min</b></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            if arrival_time <1:
                st.write(f"T-minus {arrival_seconds} seconds!")
            elif arrival_time <5:
            st.write(f"Almost here! The next train is arriving in about {arrival_time} minutes!")
            else:
            st.write(f"A little bit of a longer wait...The next train is arriving in about {arrival_time} minutes!")
    else:
        st.warning("No on-time trains at this station.")
