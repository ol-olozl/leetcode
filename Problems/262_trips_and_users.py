import pandas as pd
import numpy as np

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips = trips[(trips["request_at"]>="2013-10-01") & (trips["request_at"] <= "2013-10-03")]
    unbanned = users[users["banned"].eq("No")]
    df = trips.merge(unbanned, left_on="client_id", right_on="users_id")
    df = df.merge(unbanned, left_on="driver_id", right_on="users_id")
    df["status_update"] = np.where(
        df["status"].eq("completed"),
        0,
        1
    ) 
    grouped_df = df.groupby("request_at").agg({"status_update": "mean"}).reset_index()
    return pd.DataFrame({
        "Day": grouped_df["request_at"],
        "Cancellation Rate": np.round(grouped_df["status_update"], 2)
    })
