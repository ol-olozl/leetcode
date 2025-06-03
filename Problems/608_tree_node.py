import pandas as pd
import numpy as np

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree["type"] = np.where(tree["id"].isin(tree["p_id"]).values, "Inner", "Leaf")
    tree.loc[pd.isna(tree["p_id"]), "type"] = "Root"
    return tree[["id", "type"]]
