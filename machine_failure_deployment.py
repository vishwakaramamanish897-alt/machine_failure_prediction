import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("machine_failure_predication_model.pkl")

st.title("⚙️ Machine Failure Prediction System")

st.write("Enter sensor values to predict machine status.")

# Inputs
footfall = st.number_input("Footfall", value=0)
tempMode = st.number_input("Temp Mode", value=0)
AQ = st.number_input("AQ", value=0)
USS = st.number_input("USS", value=0)
CS = st.number_input("CS", value=0)
VOC = st.number_input("VOC", value=0)
RP = st.number_input("RP", value=0)
IP = st.number_input("IP", value=0)
Temperature = st.number_input("Temperature", value=0)

# Create dataframe with correct column order
data = [[footfall, tempMode, AQ, USS, CS, VOC, RP, IP, Temperature]]

columns = [
    "footfall",
    "tempMode",
    "AQ",
    "USS",
    "CS",
    "VOC",
    "RP",
    "IP",
    "Temperature"
]

df = pd.DataFrame(data, columns=columns)

# Prediction
if st.button("Predict Machine Status"):

    prediction = model.predict(df)

    if prediction[0] == 1:
        st.error(" Machine Will Fail")
    else:
        st.success(" Machine Will Work Properly")
 
