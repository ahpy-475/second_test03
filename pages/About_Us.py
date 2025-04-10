import streamlit as st
import lab03info as info
import time

GT_GOLD = "#B3A369"
FINAL_RIDES = 65190800

if "shown" not in st.session_state:
    st.session_state.shown = False

st.title("About the Creators")
st.write("---")
st.image(info.gatech_pic)
st.write("---")

st.header("How it Started")
st.write("Adam and Anya, both from outside Atlanta, have known there's a problem with Atlanta's public infrastructure from a young age.")
st.write("MARTA - Metropolitan Atlanta Rapid Transit Authority was founded in 1971 strictly as buses.")
st.write("Now, MARTA had 65,190,800 rides in 2024")

placeholder = st.empty()

if not st.session_state.shown:
    for i in range(62000000, FINAL_RIDES + 1, 100000):
        placeholder.metric({i,})
        time.sleep(0.0001)
    placeholder.markdown(
        f"<h1 style='color:{GT_GOLD}; font-size: 84px; font-weight: bold;'>65,190,800</h1>",
        unsafe_allow_html=True
    )
    st.session_state.shown = True
else:
    placeholder.markdown(
        f"<h1 style='color:{GT_GOLD}; font-size: 84px; font-weight: bold;'>65,190,800</h1>",
        unsafe_allow_html=True
    )

st.write("We want to solve the problem of congestion in MARTA.")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.header("Adam Haile")
    st.image(info.adam_pf_pic, width=200)
    st.write("Computer Engineering major with a concentration in Systems, Architecture, and Computer Hardware")

with col2:
    st.header("Anya Ellis")
    st.image(info.anya_pf_pic, width=200)
    st.write("Industrial and Systems Engineering major with a concentration in Operations and Supply Chain Management and a minor in Technology and Management.")
