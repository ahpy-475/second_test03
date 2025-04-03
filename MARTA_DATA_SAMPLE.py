import requests

import streamlit as st


end = "https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=f13dfc47-6bcb-4d6e-9f56-2f1d8e3ac08b"
r = requests.get(end)
data = r.json()
#st.title("This is the Current Data for MARTA")
#st.write(data)
#print(data)
des_air_list = []
des_ns_list = []
des_dora_list = []

STAT_FIVE_POINTS_STATION = []
STAT_NORTH_SPRINGS = []
STAT_AIRPORT = []
STAT_DORAVILLE = []
STAT_CHAMBLEE_STATION = []
STAT_BROOKHAVEN_STATION = []
STAT_LENOX_STATION = []
STAT_LINDBERGH_STATION = []
STAT_SAND_SPRINGS_STATION = []
STAT_DUNWOODY_STATION = []
STAT_MEDICAL_CENTER_STATION = []
STAT_BUCKHEAD_STATION = []
STAT_ARTS_CENTER_STATION = []
STAT_ARTS_CENTER_STATION = []
STAT_MIDTOWN_STATION = []
STAT_NORTH_AVE_STATION = []
STAT_CIVIC_CENTER_STATION = []
STAT_PEACHTREE_CENTER_STATION = []
STAT_CIVIC_CENTER_STATION = []
STAT_FIVE_POINTS_STATION = []
STAT_VINE_CITY_STATION = []
STAT_ASHBY_STATION = []
STAT_WEST_LAKE_STATION = []
STAT_HAMILTON_E_HOLMES_STATION = []
STAT_BANKHEAD_STATION = []
STAT_GEORGIA_STATE_STATION = []
STAT_KING_MEMORIAL_STATION = []
STAT_INMAN_PARK_STATION = []
STAT_EDGEWOOD_CANDLER_PARK_STATION = []
STAT_EAST_LAKE_STATION = []
STAT_DECATUR_STATION = []
STAT_AVONDALE_STATION = []
STAT_KENSINGTON_STATION = []
STAT_INDIAN_CREEK_STATION = []

blue_line = {}
red_line = {}
green_line = {}
gold_line = {}






for i in range(len(data)):
    if data[i]["LINE"] == "RED":

        add =  data[i]["STATION"]

        if add not in red_line:
            red_line[add] = 1
        else:
            continue

    if data[i]["LINE"] == "GOLD":
        add =  data[i]["STATION"]
        if add not in gold_line:
            gold_line[add] = 1
        else:
            continue

    if data[i]["LINE"] == "BLUE":
        add =  data[i]["STATION"]
        if add not in blue_line:
            blue_line[add] = 1
        else:
            continue

    if data[i]["LINE"] == "GREEN":
        add =  data[i]["STATION"]
        if add not in green_line:
            green_line[add] = 1
        else:
            continue
    for i in range(len(data)):
        if data[i]["DESTINATION"] == "North Springs":
            des_ns_list += [data[i]]
        elif data[i]["DESTINATION"] == "Airport":
            des_air_list += [data[i]]
        elif data[i]["DESTINATION"] == "Doraville":
            des_dora_list += [data[i]]
    #return des_air_list

    #st.write(blue_line)
   
    







