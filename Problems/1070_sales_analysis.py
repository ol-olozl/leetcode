import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    earliest_per_product = sales.groupby("product_id")["year"].min().reset_index()
    df = sales.merge(earliest_per_product, on=["product_id", "year"]).rename({"year":"first_year"}, axis=1)
    return df[["product_id", "first_year", "quantity", "price"]]
