import streamlit as st

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 11, Web Development - Section A")
st.subheader("Adam Haile, Anya Ellis")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.subheader("""Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:""")

st.write(""" 

1. MARTA Mapping – Select a train station and view real-time train arrivals. Displays a dynamic graph of train wait times. Users can filter trains by line, destination, and arrival time to plan their commute efficiently. 

2. MetroMind AI – Get personalized trip recommendations based on LIVE MARTA data! AI suggests alternative routes if there are delays and recommends nearby attractions, coffee spots, or restaurants along your route. 

3. Marty the MARTA-Bot – Chat with Marty to get real-time transit help! Ask questions like, “Which train gets me to Midtown the fastest?” or “How do I get from East Point to Kensington?” Marty provides smart, data-driven answers based on MARTA schedules. 

4. About the Creators: More information on the two people who put this project together!

""")
