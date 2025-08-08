import pandas as pd

def load_data(path="data/vahan_data.csv"):
    df = pd.read_csv(path)

    # Convert 'Year' like 201401 → datetime (Jan 2014)
    df['Date'] = pd.to_datetime(df['Year'].astype(str), format='%Y%m')
    return df
