import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on='product_id', how='left')
    df['total'] = df['quantity'] * df['price']
    gb = df.groupby('user_id').agg(spending=('total', 'sum')).reset_index()
    return gb[['user_id', 'spending']].sort_values(['spending', 'user_id'], ascending=[False, True])