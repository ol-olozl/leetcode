import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person[person["email"].duplicated()][["email"]].drop_duplicates()
    
