import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = product.merge(sales, on="product_id")
    df_target = df[df["sale_date"].between("2019-01-01", "2019-03-31")]
    df_ex = df[~df["sale_date"].between("2019-01-01", "2019-03-31")]
    ret = df_target[~df_target["product_id"].isin(df_ex["product_id"].unique())]
    return ret[["product_id", "product_name"]].drop_duplicates()
