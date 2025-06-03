import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee, left_on="managerId", right_on="id", how="left", suffixes=["_employee", "_manager"])
    employees = df[df["salary_employee"] > df["salary_manager"]]["name_employee"]
    return pd.DataFrame({"Employee": employees})
