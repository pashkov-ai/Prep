import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users['email'].str.match("^[a-zA-Z0-9_]*\@[a-zA-Z]*\.com$")]
    return df[['user_id', 'email']]