import pandas as pd

def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    metal_type = elements[elements['type'] == 'Metal'][['symbol']].rename(columns = {'symbol':'metal'})
    nonmetal_type = elements[elements['type'] == 'Nonmetal'][['symbol']].rename(columns = {'symbol':'nonmetal'})
    return metal_type.merge(nonmetal_type, how='cross')