import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors = views[views["author_id"] == views["viewer_id"]]["author_id"].unique()
    return pd.DataFrame({"id": sorted(authors)})
