import streamlit as st
import sys
import os
sys.path.append(os.path.abspath('.'))

st.set_page_config(page_title="Customer Churn Dashboard" , layout='centered')

st.title("📉 Customer Churn Prediction App")
st.markdown("""
Use the sidebar to navigate between:
- 🧮 **Analytics Dashboard**
- 🧑‍💼 **Predict Churn**
- ✏️ **Retrain Model**
""")
