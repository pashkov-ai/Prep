import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    gb = actor_director.groupby(['actor_id', 'director_id']).agg(count=('timestamp', 'count'))
    return gb[gb['count'] >= 3].reset_index()[['actor_id', 'director_id']]