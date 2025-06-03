import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df1 = request_accepted[["requester_id"]].rename(columns={"requester_id": "id"})
    df2 = request_accepted[["accepter_id"]].rename(columns={"accepter_id": "id"})
    df = pd.concat([df1, df2])
    counts = df["id"].value_counts().reset_index()
    counts.columns = ["id", "num"]
    return counts[counts["num"] == counts["num"].max()]
    
