import warnings
warnings.filterwarnings("ignore")

import requests
import json
import joblib
import pandas as pd
from preprocessAPI import data_preprocessing

def prediction(data, from_json=False):
    url = "http://127.0.0.1:5002/invocations"
    headers = {"Content-Type": "application/json"}

    if from_json:
        with open(data, 'r') as f:
            data_json = f.read()
    else:
        input_data = {
            "dataframe_split": {
                "columns": data.columns.tolist(),
                "data": data.values.tolist()
            }
        }
        data_json = json.dumps(input_data)

    response = requests.post(url, data=data_json, headers=headers)

    predictions = response.json().get("predictions")

    result_target = joblib.load("preprocessing/encoder_target.joblib")
    final_result = result_target.inverse_transform(predictions)

    return final_result[0]

columns = [
    "Credit_Mix", "Payment_of_Min_Amount", "Payment_Behaviour", "Age", "Num_Bank_Accounts", "Num_Credit_Card",
    "Interest_Rate", "Num_of_Loan", "Delay_from_due_date", "Num_of_Delayed_Payment", "Changed_Credit_Limit",
    "Num_Credit_Inquiries", "Outstanding_Debt", "Monthly_Inhand_Salary", "Monthly_Balance",
    "Amount_invested_monthly", "Total_EMI_per_month", "Credit_History_Age"
]

data = ["Good", "No", "Low_spent_Small_value_payments", 23, 3, 4, 3, 4, 3, 7, 11.27, 5, 809.98, 1824.80, 186.26, 236.64, 49.50, 216]
df = pd.DataFrame([data], columns=columns)

new_data = data_preprocessing(data=df)

# Predict
print("Prediction from raw DataFrame:")
print(prediction(new_data))

print("\nPrediction from input.json (preprocessed):")
print(prediction("input.json", from_json=True))