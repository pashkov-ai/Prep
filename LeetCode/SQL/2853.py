import pandas as pd

def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
    eng_s = salaries[salaries['department'] == 'Engineering']['salary'].max()
    mar_s = salaries[salaries['department'] == 'Marketing']['salary'].max()
    return pd.DataFrame([[abs(eng_s - mar_s)]], columns=['salary_difference'])