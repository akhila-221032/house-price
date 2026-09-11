import pandas as pd
import joblib
import streamlit as st

model=joblib.load("house_price.pkl")
# Title
st.title("🏠 House Price Prediction ")

st.header("Welcome to House Price Prediction App -💰 Know the Value of Your Home")

st.subheader(" 📊 “Predict smarter. Invest better.”")

st.write("“Data-driven insights for smarter property decisions.")

a=st.text_input("can i know your good name?😄")
st.write("hello", a,"welcome")

st.info("Please enter the following details to predict the median house value:")
# Inputs

longitude = st.number_input(
    "Longitude",
    value=-122.23
)

latitude = st.number_input(
    "Latitude",
    value=37.88
)

housing_median_age = st.text_input(
    "Housing Median Age"
)

total_rooms = st.text_input(
    "Total Rooms(800<)",
    
)

total_bedrooms = st.text_input(
    "Total Bedrooms",
    value=200
)

population = st.text_input(
    "Population(200-1200)",
    value=300
)

households = st.number_input(
    "Households",
    min_value=1.0,
    value=150.0
)

median_income = st.number_input(
    "Median Income",
    min_value=0.0,
    value=3.0
)

# Prediction
if st.button("Predict House Price"):

    # Create input DataFrame
    input_data = pd.DataFrame([[
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income
    ]], columns=[
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income"
    ])

    with st.spinner("🔮 Predicting house price..."):
        # Make prediction
        prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )
    st.balloons()
    st.info("Thank you for using the House Price Prediction App! 🏡💰")

   

    