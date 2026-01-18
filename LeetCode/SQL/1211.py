import pandas as pd
# The judge throws an error in certain rounding operations on what seems to be a bug with pandas's rounding results. For example, round(4.5) = 4, but round(5.5) = 6
# Actually, it's not a bug, it's a feature. Pandas follows the "round to even" rule intentionally, because it reduces the bias in rounding.
# For example: average(1.5, 2.5, 3.5, 4.5, 5.5) = 3.5
# rounding up: average(2, 3, 4, 5, 6) = 4.0
# rounding to even: average(2, 2, 4, 4, 6) = 3.6

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries.rating / queries.position
    queries['poor_query_percentage'] = (queries.rating < 3) * 100

    gb = queries.groupby('query_name')[['quality', 'poor_query_percentage']].mean().round(2)
    return gb.reset_index()