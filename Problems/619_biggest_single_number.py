import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    n_counts = my_numbers["num"].value_counts().reset_index()
    biggest = n_counts[n_counts["count"] == 1]["num"].values.max()
    return pd.DataFrame({"num": [biggest]})
