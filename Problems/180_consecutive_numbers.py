import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["prev1"] = logs["num"].shift(1)
    logs["prev2"] = logs["num"].shift(2)
    df = logs[(logs["num"]==logs["prev1"]) & (logs["num"]==logs["prev2"])]["num"].drop_duplicates()
    return pd.DataFrame({"ConsecutiveNums": df})
