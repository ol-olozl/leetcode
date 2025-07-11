import pandas as pd

def article_views_I(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"] == views["viewer_id"]]
    ret = df.groupby(["author_id", "view_date"]).size().reset_index(name="count")
    ids = ret[ret["count"] > 1]["author_id"].drop_duplicates().sort_values()
    return pd.DataFrame({"id": ids})
