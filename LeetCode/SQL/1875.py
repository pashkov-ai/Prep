import pandas as pd

def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.copy()

    # COUNT(*) OVER (PARTITION BY salary)
    df["cnt"] = df.groupby("salary")["salary"].transform("count")

    # filter salaries that appear more than once
    df = df[df["cnt"] > 1]

    # DENSE_RANK() OVER (ORDER BY salary)
    df["team_id"] = df["salary"].rank(method="dense").astype(int)

    # final ordering
    df = df.sort_values(["team_id", "employee_id"])

    # select columns
    result = df[["employee_id", "name", "salary", "team_id"]]
    return result