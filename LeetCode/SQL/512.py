import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(['player_id', 'event_date'])
    gb = df.groupby('player_id', sort=False).agg(device_id=('device_id', lambda x: list(x)[0]))
    return gb.reset_index()