from src.metrics import profit_factor
import pandas as pd

def generate_md_report(df, filename='./output/Report_statement.html'):
    profit_factor_df = profit_factor(df)
    df_sorted = profit_factor_df.sort_values(by='Profit Factor', ascending=False).copy()
    
    styler = df_sorted.style \
        .format("{:.2f}") \
        .background_gradient(cmap='RdYlGn', subset=['Profit Factor']) \
        .bar(subset=['Gross Profit'], color='#90ee90') \
        .bar(subset=['Gross Loss'], color='#ffcccb')

    html_table = styler.to_html()

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_table)
