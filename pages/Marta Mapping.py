import streamlit as st
import requests
import pandas as pd
import MARTA_DATA_SAMPLE as count
import altair as alt
st.title("MARTA Many & Much")
#st.set_page_config(page_title="MARTA Many & Much", layout="wide")

API_URL = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"

def fetch_marta_data():
    info = requests.get(API_URL)
    data = info.json()
    return data
red_count = 0
blue_count = 0
green_count = 0
gold_count = 0
train_data = fetch_marta_data()
stations = sorted(set(train.get("STATION", "Unknown") for train in train_data))
st.header("How MANY lines?")
st.write("This is how many train stations are at each line!")
red_list = []
blue_list = []
green_list = []
gold_list = []
color_scale = alt.Scale(
    domain=["RED", "BLUE", "GREEN", "GOLD"],
    range=["#ff0000", "#0000ff", "#00ff00", "#B3A369"])
amount = st.slider("Select Number of trains to add", 0, 50, key="slider")

for train in count.red_line:
    red_list.append(train)
    red_count = len(red_list)
for train in count.blue_line:
    blue_list.append(train)
    blue_count = len(blue_list)
for train in count.green_line:
    green_list.append(train)
    green_count = len(green_list)
for train in count.gold_line:
    gold_list.append(train)
    gold_count = len(gold_list)

col1, col2, col3, col4 = st.columns(4)
if "red_count" not in st.session_state:
    st.session_state.red_count = red_count
if "blue_count" not in st.session_state:
    st.session_state.blue_count = blue_count
if "green_count" not in st.session_state:
    st.session_state.green_count = green_count
if "gold_count" not in st.session_state:
    st.session_state.gold_count = gold_count
with col1:
    if st.button("Add Red Train"):
        st.session_state.red_count += amount
        st.success(f"Hooray! Now there are {st.session_state.red_count} Red trains")

with col2:
    if st.button("Add Blue Train"):
        st.session_state.blue_count += amount
        st.success(f"Hooray! Now there are {st.session_state.blue_count} Blue trains!")

with col3:
    if st.button("Add Green Train"):
        st.session_state.green_count += amount
        st.success(f"Hooray! Now there are {st.session_state.green_count} Green trains!")

with col4:
    if st.button("Add Gold Train"):
        st.session_state.gold_count += amount
        st.success(f"Hooray! Now there are {st.session_state.gold_count} Gold trains!")


source = pd.DataFrame({
    "MARTA Line": ["RED", "BLUE", "GREEN", "GOLD"],  
    "Number of Trains": [st.session_state.red_count,st.session_state.blue_count, st.session_state.green_count, st.session_state.gold_count]
})

bar_chart = alt.Chart(source).mark_bar().encode(
    x=alt.X("MARTA Line", sort=None),
    y="Number of Trains",
    color=alt.Color("MARTA Line", scale=color_scale)
).properties(
    width=600,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)





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
