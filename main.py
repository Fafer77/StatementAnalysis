import pandas as pd
from src.data_loader import read_report_mt5
from src.metrics import profit_factor
from src.report_generator import generate_html_report
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

if __name__=='__main__':
    # filepath = input('Enter Filepath: ')
    transactions_df = read_report_mt5(filepath='./testData/ReportHistory.xlsx')
    generate_html_report(transactions_df)

