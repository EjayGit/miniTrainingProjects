import pandas as pd

data = pd.read_csv("Sales.csv")
print(data)
newData = data.groupby(["customer_id", "salesman_id"]).agg({"amount":["sum", "count"]})
newData.columns = ["sum2", "count"]
print(newData)
newData.to_csv("csvChallenge.csv")