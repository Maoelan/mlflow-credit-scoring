import json
import mlflow
import pandas as pd

with open("data.json", "r") as file:
    data = json.load(file)

input_data = {
    "dataframe_split": {
        "columns": data["columns"],
        "data": data["data"]
    }
}

model_uri = 'runs:/eedc1b064fa446b6b8d04b6177f7f266/model'
model = mlflow.pyfunc.load_model(model_uri)

df = pd.DataFrame(input_data["dataframe_split"]["data"], columns=input_data["dataframe_split"]["columns"])

pred = model.predict(df)

print(pred)
