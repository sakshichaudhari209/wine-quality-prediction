import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("wine_quality_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="centered"
)


st.title("🍷 Wine Quality Prediction System")

st.write(
    "Enter the chemical properties of the wine "
    "to predict its quality."
)


# Input fields

fixed_acidity = st.number_input(
    "Fixed Acidity",
    min_value=0.0,
    value=7.4
)

volatile_acidity = st.number_input(
    "Volatile Acidity",
    min_value=0.0,
    value=0.70
)

citric_acid = st.number_input(
    "Citric Acid",
    min_value=0.0,
    value=0.0
)

residual_sugar = st.number_input(
    "Residual Sugar",
    min_value=0.0,
    value=1.9
)

chlorides = st.number_input(
    "Chlorides",
    min_value=0.0,
    value=0.076
)

free_sulfur_dioxide = st.number_input(
    "Free Sulfur Dioxide",
    min_value=0.0,
    value=11.0
)

total_sulfur_dioxide = st.number_input(
    "Total Sulfur Dioxide",
    min_value=0.0,
    value=34.0
)

density = st.number_input(
    "Density",
    min_value=0.0,
    value=0.9978
)

pH = st.number_input(
    "pH",
    min_value=0.0,
    value=3.51
)

sulphates = st.number_input(
    "Sulphates",
    min_value=0.0,
    value=0.56
)

alcohol = st.number_input(
    "Alcohol",
    min_value=0.0,
    value=9.4
)


# Quality category function

def get_quality_category(quality):

    if quality <= 4:
        return "Poor"

    elif quality == 5:
        return "Average"

    elif quality == 6:
        return "Good"

    else:
        return "Excellent"


# Prediction

if st.button("Predict Wine Quality"):

    input_data = pd.DataFrame([{
        "fixed acidity": fixed_acidity,
        "volatile acidity": volatile_acidity,
        "citric acid": citric_acid,
        "residual sugar": residual_sugar,
        "chlorides": chlorides,
        "free sulfur dioxide": free_sulfur_dioxide,
        "total sulfur dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol
    }])


    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100

    category = get_quality_category(prediction)


    st.success(
        f"Predicted Wine Quality: {prediction}"
    )

    st.info(
        f"Quality Category: {category}"
    )

    st.write(
        f"Prediction Confidence: {confidence:.2f}%"
    )