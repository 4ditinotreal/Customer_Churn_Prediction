import streamlit as st
import pandas as pd
import pickle

from utils import encode_input
from logger import setup_logger

logger = setup_logger("Predict Churn")

st.title("📉 Predict Customer Churn")

# --- Load Model ---
try:
    with open("model/churn_model.pkl", "rb") as f:
        model = pickle.load(f)
        logger.info("Model has been loaded.")

    with open("model/feature_names.pkl", "rb") as f:
        feature_order = pickle.load(f)
        logger.info("Feature names have been loaded.")
except Exception as e:
    logger.error(e)
    logger.error("Error has occurred")
    st.error("Model not found. Please retrain first.")
    st.stop()

# --- Input Form ---
try:
    st.sidebar.header("Customer Input")

    input_data = {
        "gender": st.sidebar.selectbox("Gender", ["Male", "Female"]),
        "SeniorCitizen": st.sidebar.selectbox("Senior Citizen", [0, 1]),
        "Partner": st.sidebar.selectbox("Partner", ["Yes", "No"]),
        "Dependents": st.sidebar.selectbox("Dependents", ["Yes", "No"]),
        "tenure": st.sidebar.slider("Tenure", 0, 72, 24),
        "Contract": st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"]),
        "MonthlyCharges": st.sidebar.slider("Monthly Charges", 0.0, 150.0, 70.0),
        "TotalCharges": st.sidebar.slider("Total Charges", 0.0, 2500.0, 1000.0)
    }

    input_df = pd.DataFrame([input_data])
    input_df = encode_input(input_df)
    input_df = input_df[feature_order]

    if st.button("Predict"):
        probability = model.predict_proba(input_df)[0][1]

        st.subheader(f"🔮 Churn Probability: **{round(probability * 100, 2)}%**")

        if probability > 0.7:
            st.error("❗ High Risk of Churn")
        elif probability > 0.4:
            st.warning("⚠️ Medium Risk of Churn")
        else:
            st.success("✅ Low Risk of Churn")

except Exception as e:
    logger.error(e)
    logger.error("Error has occurred")
    st.error("Something went wrong during prediction.")
