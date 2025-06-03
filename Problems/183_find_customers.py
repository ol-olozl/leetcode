import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(customers, left_on="customerId", right_on="id", how="right", suffixes=["_order", "_customer"])
    df = df[pd.isna(df["id_order"])]
    return pd.DataFrame({"Customers": df["name"]})
