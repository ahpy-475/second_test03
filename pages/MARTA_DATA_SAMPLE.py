import requests
import streamlit as st

end = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"
r = requests.get(end)
data = r.json()
st.title("This is the Current Data for MARTA")
st.write(data)

