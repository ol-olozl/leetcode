import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer.drop_duplicates(inplace=True)
    df = customer.groupby("customer_id")["product_key"].count().reset_index()
    df.columns = ["customer_id", "count"]
    df = df[df["count"].eq(len(product))]
    return df[["customer_id"]]
