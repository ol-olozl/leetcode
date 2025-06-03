import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red = company[company["name"].eq("RED")]
    df = orders.merge(red, on="com_id").merge(sales_person, on="sales_id", how="right")
    df = df[pd.isna(df["com_id"])].rename(columns={"name_y":"name"})
    return df[["name"]]
