import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
	df = employee["salary"].sort_values(ascending=False).drop_duplicates()
	second = df.iloc[1] if len(df) > 1 else None
	return pd.DataFrame({"SecondHighestSalary": [second]})
