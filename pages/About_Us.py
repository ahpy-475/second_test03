import streamlit as st
import lab03info as info

st.title("About the Creators")
st.write("---")
st.image(info.gatech_pic)
st.write("---")

st.header("How it Started")
st.write("Adam and Anya, both from outside Atlanta, have known there's a problem with Atlanta's public infrastructure from a young age.")
st.write("MARTA - Metropolitan Atlanta Rapid Transit Authority was founded in 1971 strictly as buses.")
st.write("Now, MARTA had 65,190,800 rides in 2024")
st.write("We want to solve the problem of congestion in MARTA.")
st.write("---")

col1, col2 = st.columns(2)

with col1:
  st.header("Adam Haile")
  st.image(info.adam_pf_pic, width = 200)
  st.write("Computer Engineering major with a concentration in Systems, Architecture, and Computer Hardware")

with col2:
  st.header("Anya Ellis")
  st.image(info.anya_pf_pic, width = 200)
  st.write("Industrial and Systems Engineering major with a concentration in Operations and Supply Chain Management and a minor in Technology and Management.")
