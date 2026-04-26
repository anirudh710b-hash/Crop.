import streamlit as st
import numpy as np
import pickle

# Page title
st.title("Crop Recommendation System")

st.write("Enter soil and weather details to get crop recommendation")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# User Inputs
N = st.number_input("Nitrogen (N)", min_value=0)

P = st.number_input("Phosphorus (P)", min_value=0)

K = st.number_input("Potassium (K)", min_value=0)

temperature = st.number_input("Temperature (°C)")

humidity = st.number_input("Humidity (%)")

ph = st.number_input("Soil pH")

rainfall = st.number_input("Rainfall (mm)")


# Prediction Button
if st.button("Predict Crop"):

    features = np.array([[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]])

    prediction = model.predict(features)

    st.success(f"Recommended Crop: {prediction[0]}")