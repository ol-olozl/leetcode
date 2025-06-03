import pandas as pd
import numpy as np

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=["player_id", "event_date"], inplace=True)
    logins = activity.groupby("player_id")["event_date"].min().reset_index()
    df = activity.merge(logins, on="player_id", suffixes=["_activity", "_first"])
    df["next_day"] = df["event_date_first"] + pd.Timedelta(days=1)
    fraction = df[df["event_date_activity"] == df["next_day"]]["player_id"].nunique() / df["player_id"].nunique()
    return pd.DataFrame({"fraction": [np.round(fraction, 2)]})
