import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    gb = rides.groupby('user_id').agg(travelled_distance=('distance', 'sum'))
    df = users.merge(gb, left_on='id', right_on='user_id', how='left')
    df['travelled_distance'].fillna(0, inplace=True)
    return df[['name', 'travelled_distance']].sort_values(['travelled_distance', 'name'], ascending=[False, True])