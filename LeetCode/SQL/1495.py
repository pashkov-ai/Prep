import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    content['content_id'] = content['content_id'].astype(int)
    df = tv_program.merge(content, on='content_id', how='left')
    df = df[(df['Kids_content'] == 'Y') & (df['content_type'] == 'Movies')
        & (df['program_date'].dt.month == 6) & (df['program_date'].dt.year == 2020)]
    return df[['title']].drop_duplicates(['title'])