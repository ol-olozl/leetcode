import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on="departmentId", right_on="id", suffixes=["_employee", "_department"])
    df["rank"] = df.groupby("name_department")[["salary"]].rank(method="dense", ascending=False)
    df = df[df["rank"] <= 3]
    return pd.DataFrame({
        "Department": df["name_department"],
        "Employee": df["name_employee"],
        "Salary": df["salary"]
    })
