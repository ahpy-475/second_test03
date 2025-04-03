import streamlit as st
import requests
#import matplotlib.pyplot as plt

st.set_page_config(page_title="MARTA Mapping", layout="wide")

API_URL = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"

def fetch_marta_data():
    info = requests.get(API_URL)
    data = info.json()

    return data

train_data = fetch_marta_data()

stations = sorted(set(train.get("STATION", "Unknown") for train in train_data))

st.title("MARTA Times")
st.write("Select your station to see which trains are arriving **next**")

selected_station = st.selectbox(" Choose Your Station:", ["Choose a station"] + stations)

if selected_station and selected_station != "Choose a station":
    st.subheader(f"Time until next train arrives at **{selected_station}:**")

    trains_at_station = [train for train in train_data if train.get("STATION") == selected_station]

    if trains_at_station:
        cols = st.columns(2)  # Two-column layout

        for i, train in enumerate(trains_at_station):
            arrival_seconds = int(train.get("WAITING_SECONDS", "0"))
            arrival_time = round(int(arrival_seconds) / 60)  
            
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
