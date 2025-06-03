import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    atts = insurance[insurance.duplicated(subset=["lat", "lon"], keep=False)]["pid"].values
    nunique = insurance.groupby("tiv_2015")["pid"].count().reset_index()
    nunique = nunique[nunique["pid"] > 1]["tiv_2015"].values
    total = insurance[insurance["tiv_2015"].isin(nunique) & ~insurance["pid"].isin(atts)]["tiv_2016"].sum()
    return pd.DataFrame({"tiv_2016": [total]})
