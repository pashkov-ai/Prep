import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on = 'product_id', how='left')
    iphone_buyers = df[df['product_name'] == 'iPhone']['buyer_id'].unique()
    return df[(df['product_name'] == 'S8') & (~df['buyer_id'].isin(iphone_buyers))][['buyer_id']].drop_duplicates()