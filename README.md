# 📉 Customer Churn Prediction Dashboard

A Machine Learning-based web application built with **Streamlit** to predict customer churn, visualize customer insights, and retrain the prediction model using new datasets.

---

## 🚀 Features

- 📊 Interactive Analytics Dashboard
- 🤖 Customer Churn Prediction
- 🔄 Retrain Machine Learning Model
- 📁 Upload new CSV datasets
- 📈 Data Visualization
- 💾 Save updated trained model automatically

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Matplotlib

---

## 📂 Project Structure

```
Customer_Churn_Prediction/
│
├── App.py
├── utils.py
├── logger.py
├── dashboard.log
├── README.md
│
├── pages/
│   ├── Analytics_Dashboard.py
│   ├── Predict_Churn.py
│   └── Retrain_Model.py
│
├── model/
│   ├── churn_model.pkl
│   └── feature_names.pkl
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/4ditinotreal/Customer_Churn_Prediction.git
```

Move into the project folder:

```bash
cd Customer_Churn_Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas numpy scikit-learn plotly matplotlib
```

---

## ▶️ Run the Application

```bash
streamlit run App.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📊 Modules

### 📈 Analytics Dashboard

- Customer Overview
- Churn Analysis
- Interactive Charts
- Data Filters

### 🤖 Predict Churn

Predict whether a customer is likely to churn based on customer information.

### 🔄 Retrain Model

- Upload a new CSV dataset
- Retrain the Random Forest model
- Save the updated model automatically

---

## 🤖 Machine Learning

Model Used:

- Random Forest Classifier

Evaluation:

- Train/Test Split
- Label Encoding
- Feature Encoding

---

## 📁 Dataset

Dataset:

**Telco Customer Churn Dataset**

Source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## 👨‍💻 Author

**Aditi Thul**

GitHub:
https://github.com/4ditinotreal

---

## 📄 License

This project is licensed under the MIT License.