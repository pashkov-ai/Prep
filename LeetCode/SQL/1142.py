import pandas as pd
from datetime import datetime, timedelta

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    end_date = datetime.strptime('2019-07-27', "%Y-%m-%d")
    start_date = end_date - timedelta(days=30-1)

    df = activity[(start_date <= activity['activity_date']) & (activity['activity_date'] <= end_date)]
    sessions_count = df.drop_duplicates(['user_id', 'session_id']).groupby('user_id').agg(count=('session_id', 'count'))
    value = 0
    if len(sessions_count) > 0:
        value = sessions_count['count'].mean()
    return pd.DataFrame([[value]], columns=['average_sessions_per_user']).round(2)