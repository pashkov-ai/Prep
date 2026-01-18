import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(departments, left_on='department_id', right_on='id', how='left', suffixes=['', '_department'])
    return df[df['name_department'].isna()][['id', 'name']]