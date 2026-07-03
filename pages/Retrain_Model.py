import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from utils import encode_input
from logger import setup_logger

logger = setup_logger("Retrain Model")

st.title("🔄 Retrain Model with New Data")
logger.info("Retraining website loaded")

uploaded = st.file_uploader("📁 Upload New CSV File", type="csv")

if uploaded:
    try:
        # Read and clean data
        df = pd.read_csv(uploaded)  
        logger.info("Dataset has been uploaded")

        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df.dropna(inplace=True)
        logger.info("Null values have been dropped")

        df.drop(columns=["customerID"], errors="ignore", inplace=True)
        logger.info("CustomerID column has been dropped")

        st.success("✅ File uploaded and cleaned successfully.")

        # Show data preview
        st.subheader("📄 Preview of Uploaded Data")
        logger.info(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
        st.dataframe(df.head())

        # Selected features to use
        selected_features = [
            "gender", "SeniorCitizen", "Partner", "Dependents",
            "tenure", "Contract", "MonthlyCharges", "TotalCharges"
        ]

        # Check if required columns exist
        if not set(selected_features + ["Churn"]).issubset(df.columns):
            logger.error("❌ Uploaded file is missing required columns.")
            st.error("❌ Uploaded file is missing required columns.")
            st.stop()

        # Train button
        if st.button("🚀 Retrain Model Now"):
            try:
                X = encode_input(df[selected_features])
                y = LabelEncoder().fit_transform(df["Churn"])

                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42)

                model = RandomForestClassifier(n_estimators=100)
                model.fit(X_train, y_train)
                logger.info("✅ Model fitting has been completed.")

                # Save model
                with open("model/churn_model.pkl", "wb") as f:
                    pickle.dump(model, f)
                    logger.info("🧠 Model has been saved")

                # Save feature names
                with open("model/feature_names.pkl", "wb") as f:
                    pickle.dump(list(X.columns), f)
                    logger.info("📦 Feature names have been saved")

                st.success("✅ Model retrained and saved successfully!")

            except Exception as e:
                logger.error(e)
                st.error("❌ Error during model retraining.")
    except Exception as ex:
        logger.error(ex)
        st.error("❌ Error while processing file.")
