import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, on="empId", how="left").fillna(-10000)
    df = df[df["bonus"] < 1000].replace({-10000: None})
    return df[["name", "bonus"]]
