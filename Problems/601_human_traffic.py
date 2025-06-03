import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium.sort_values(by="id", inplace=True)
    df = stadium[stadium["people"] >= 100]
    df["row"] = df["id"].rank()
    df["diff"] = df["row"] - df["id"]
    grouped = df.groupby("diff")["id"].count().reset_index()
    diffs = grouped[grouped["id"] >=3]["diff"].values
    ret = df[df["diff"].isin(diffs)]
    return ret[["id", "visit_date", "people"]]
