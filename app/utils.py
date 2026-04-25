import pandas as pd
import numpy as np
from pathlib import Path

@st.cache_data
def load_data():
    """Load and cache all country data"""
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    all_data = {}
    
    for country in countries:
        file_path = Path(f'data/{country}_clean.csv')
        if file_path.exists():
            df = pd.read_csv(file_path)
            df['Date'] = pd.to_datetime(df['Date'])
            df['Country'] = country.capitalize()
            all_data[country.capitalize()] = df
    
    if all_data:
        combined_df = pd.concat(all_data.values(), ignore_index=True)
        combined_df['Year'] = combined_df['Date'].dt.year
        combined_df['Month'] = combined_df['Date'].dt.month
        return combined_df
    return pd.DataFrame()

@st.cache_data
def filter_data(df, countries, year_range, variable):
    """Filter data based on user selections"""
    filtered = df[df['Country'].isin(countries)]
    filtered = filtered[(filtered['Year'] >= year_range[0]) & 
                        (filtered['Year'] <= year_range[1])]
    return filtered