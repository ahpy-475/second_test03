import requests

#import streamlit as st


def Destinations():
    end = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"
    r = requests.get(end)
    data = r.json()
    #st.title("This is the Current Data for MARTA")
    #st.write(data)
    #print(data)
    des_air_list = []
    des_ns_list = []
    des_dora_list = []


    for i in range(len(data)):
        if data[i]["DESTINATION"] == "North Springs":
            des_ns_list += [data[i]]
        elif data[i]["DESTINATION"] == "Airport":
            des_air_list += [data[i]]
        elif data[i]["DESTINATION"] == "Doraville":
            des_dora_list += [data[i]]
    #return des_air_list
    st.write("This is the data for each train that has the destination of the Airport")
    for i in des_air_list:
      st.write(i)

    st.write("This is the data for each train that has the destination of North Springs")
    for i in des_ns_list:
        st.write(i)

    st.write("This is the data for each train that has the destination of Doraville")
    for i in des_dora_list:
        st.write(i)


Destinations()





