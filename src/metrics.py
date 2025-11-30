import seaborn as sns
import numpy as np
import pandas as pd

def profit_factor(transactions_df):
    transactions_df['Net Profit'] = transactions_df['Swap'] + transactions_df['Profit'] + transactions_df['Commission']

    gross_profit_fn = lambda x: x[x >= 0].sum()
    gross_loss_fn = lambda x: x[x < 0].sum()

    stats = transactions_df.groupby('Symbol')['Net Profit'].agg([
        gross_profit_fn,
        gross_loss_fn
    ])

    stats.columns = ['Gross Profit', 'Gross Loss']
    stats['Profit Factor'] = round(abs(stats['Gross Profit'] / stats['Gross Loss'].replace(0, 1)), 2)
    print(stats)

    return stats
