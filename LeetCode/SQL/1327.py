import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders[(orders.order_date.dt.year == 2020) & (orders.order_date.dt.month == 2)]
    df = df.merge(products, how='left', on='product_id')
    gb = df.groupby('product_name')[['unit']].sum().reset_index()
    return gb[gb.unit >= 100]