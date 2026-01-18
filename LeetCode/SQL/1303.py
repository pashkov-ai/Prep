import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    gb = employee.groupby('team_id').agg(team_size = ('employee_id', 'count')).reset_index()
    return employee.merge(gb, on='team_id', how='left')[['employee_id', 'team_size']]