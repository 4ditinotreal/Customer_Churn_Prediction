import pandas as pd

def load_data(path="data/WA_Fn-UseC_-Telco-Customer-Churn.csv"):
    df = pd.read_csv(path)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)
    return df
def encode_input(df):
    mapping = {
        'Male': 1, 'Female': 0,
        'Yes': 1, 'No': 0,
        'Month-to-month': 0, 'One year': 1, 'Two year': 2
    }
    return df.replace(mapping)

