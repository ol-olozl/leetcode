import pandas as pd
import numpy as np

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee, on="employee_id")
    avg_years = df.groupby("project_id")["experience_years"].mean().reset_index().rename({"experience_years": "average_years"}, axis=1)
    avg_years["average_years"] = np.round(avg_years["average_years"], 2)
    return avg_years
