import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']].sort_values('author_id').drop_duplicates('author_id')
    return df.rename(columns={'author_id': 'id'})[['id']]