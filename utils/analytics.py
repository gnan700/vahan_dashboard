import pandas as pd

def compute_growth(df):
    df['Quarter'] = df['Date'].dt.to_period('Q')
    df_grouped = df.groupby(['Quarter', 'VehicleType', 'Manufacturer'])['Registrations'].sum().reset_index()
    df_grouped.sort_values(by=['VehicleType', 'Manufacturer', 'Quarter'], inplace=True)
    df_grouped['QoQ Growth (%)'] = df_grouped.groupby(['VehicleType', 'Manufacturer'])['Registrations'].pct_change().round(3) * 100
    df_grouped['YoY Growth (%)'] = df_grouped.groupby(['VehicleType', 'Manufacturer'])['Registrations'].pct_change(4).round(3) * 100
    return df_grouped