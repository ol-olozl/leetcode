import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on="departmentId", right_on="id", suffixes=["_employee", "_department"])
    max_salary = df.groupby("name_department")["salary"].max().reset_index()
    top_earner = df.merge(max_salary, on=["name_department", "salary"])
    return pd.DataFrame({
        "Department": top_earner["name_department"],
        "Employee": top_earner["name_employee"],
        "Salary": top_earner["salary"]
    })
