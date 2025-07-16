import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    goal: find employees who have the highest salary in each of the departments
    steps:
    1) merge Employee and Department tables on department id
    2) find employees where their salary is same as department id's max salary
    3) return the result  
    """
    df = employee.merge(department, how="left", left_on="departmentId", right_on="id")
    df_max = df.loc[df.groupby("departmentId")["salary"].transform("max") == df["salary"]]
    df_max.rename(columns={"name_y": "Department", "name_x":"Employee", "salary": "Salary"}, inplace=True)
    return df_max[["Department", "Employee", "Salary"]]
