import pandas as pd
import numpy as np

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat["prev"] = seat["student"].shift(1)
    seat["next"] = seat["student"].shift(-1)
    seat["next"].fillna(seat["student"], inplace=True)
    seat["updated"] = np.where(
        seat["id"]%2 == 0,
        seat["prev"],
        seat["next"]
    )
    seat = seat.sort_values("id")
    return pd.DataFrame({"id": seat["id"], "student": seat["updated"]})
