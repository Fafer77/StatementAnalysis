import pandas as pd

def read_report_mt5(filepath):
    try:
        file = pd.read_excel(filepath, header=None)
    except Exception as e:
        print(f'Error opening file: {e}')
        return None

    start_row = None
    end_row = None

    for idx, row in file.iterrows():
        row_strs = row.astype(str).values
        if 'Positions' in row_strs:
            start_row = idx + 1
        elif start_row is not None:
            if 'Orders' in row_strs or 'Deals' in row_strs:
                end_row = idx - 1
                break
    
    if start_row is None:
        return None
    
    if end_row is None:
        end_row = len(file)
    
    print('Reading Positions Sector from MT5 statement...')
    sector_length = end_row - start_row
    df_clean = pd.read_excel(filepath, header=0, skiprows=start_row, nrows=sector_length)
    df_clean.rename(columns={
        'S / L': 'SL', 'T / P': 'TP', 'Time.1': 'Time', 'Price.1': 'Price'},
        inplace=True)
    
    return df_clean