import streamlit as st
import lab03info as info

st.title("About the Creators")
st.write("---")
st.image(info.gatech_pic)
st.write("---")


st.header("Adam Haile")
st.image(info.adam_pf_pic, width = 200)
st.write("Computer Engineering major with a concentration in Systems, Architecture, and Computer Hardware")
st.write("---")

st.header("Anya Ellis")
st.image(info.anya_pf_pic, width = 200)
st.write("Industrial and Systems Engineering major with a concentration in Operations and Supply Chain Management and a minor in Technology and Management.")