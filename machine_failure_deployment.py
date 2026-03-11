

import streamlit as st
import pandas as pd
import  joblib


model = joblib.load("machine_failure_predication_model.pkl")

st.title("Machine failure prediction system")

st.write("you can enter the data from senson and check whether your machine will work or fail under certain condition")

footfall = st.number_input("footfall")
tempMode = st.number_input("tempMode")
aq = st.number_input("AQ")
uss = st.number_input("USS")
cs = st.number_input("CS")
voc = st.number_input("VOC")
rp = st.number_input("RP")
ip = st.number_input("IP")
temperature = st.number_input("Temperature")

df = pd.DataFrame({
    "footfall":[footfall],
    "tempMode":[tempMode],
    "AQ":[aq],
    "USS":[uss],
    "VOC":[voc],
    "RP":[rp],
    "IP":[ip],
    "Temperature":[temperature]

})

if st.button("predict"):
    prediction = model.predict(df)
    if prediction[0] == 1: 
        st.error("Machine will fail")
    else:
        st.success("Machine will work")
