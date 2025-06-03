import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby("customer_number")["order_number"].count().reset_index()
    ret = df[df["order_number"] == df["order_number"].max()]
    return ret[["customer_number"]]
