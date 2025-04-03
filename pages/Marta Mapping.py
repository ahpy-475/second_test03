import streamlit as st
import requests
st.title("MARTA Many & Much")
#st.set_page_config(page_title="MARTA Many & Much", layout="wide")

API_URL = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"

def fetch_marta_data():
    info = requests.get(API_URL)
    data = info.json()
    return data

train_data = fetch_marta_data()
stations = sorted(set(train.get("STATION", "Unknown") for train in train_data))
st.header("How MANY lines")
st.write("This is how many train stations are at each line!")

st.header("How MUCH time?")
st.write("Select your station to see which trains are arriving **next**")

selected_station = st.selectbox("Choose Your Station:", ["Choose a station"] + stations)

if selected_station and selected_station != "Choose a station":
    st.subheader(f"Time until next train arrives at **{selected_station}:**")

    trains_at_station = [train for train in train_data if train.get("STATION") == selected_station]

    if trains_at_station:
        cols = st.columns(2)  

        for i, train in enumerate(trains_at_station):
            arrival_seconds = int(train.get("WAITING_SECONDS", "0"))
            arrival_time = round(arrival_seconds / 60)

            if train.get("LINE") == "RED":
                box_color = "#ff0000"
            elif train.get("LINE") == "BLUE":
                box_color = "#0000ff"
            elif train.get("LINE") == "GREEN":
                box_color = "#00ff00"
            elif train.get("LINE") == "GOLD":
                box_color = "#B3A369"
            else:
                box_color = "#808080" 

            with cols[i % 2]:  
                st.markdown(
                    f"""
                    <div style="background-color:{box_color}; color:white; padding:15px; border-radius:10px; text-align:center; margin-bottom:10px;">
                        <h3>{train.get('LINE')} Line</h3>
                        <p> "Train #{train.get("TRAIN_ID")}" <b>Arriving in {arrival_time} min</b></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if arrival_seconds < 61:
                    st.write(f"T-minus {arrival_seconds} seconds!")
                elif arrival_seconds < 6000:
                    minutes = round(arrival_seconds / 60)
                    st.write(f"Almost here! This train is arriving in about {minutes} minutes!")
                else:
                    minutes = round(arrival_seconds / 60)
                    st.write(f"A little bit of a longer wait...The next train is arriving in about {minutes} minutes!")
    else:
        st.warning("No on-time trains at this station.")
