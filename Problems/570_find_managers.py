import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId")["id"].count().reset_index()
    df = df.merge(employee, left_on="managerId", right_on="id", suffixes=["_num", ""])
    return df[df["id_num"] >= 5][["name"]]
