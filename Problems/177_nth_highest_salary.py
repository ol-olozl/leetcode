import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee["salary"].sort_values(ascending=False).drop_duplicates()
    nth = df.iloc[N-1] if (len(df) >= N) and (N > 0) else None
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth]})
