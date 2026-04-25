# app/main.py - Matplotlib version (NO plotly needed)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(page_title="African Climate Dashboard", layout="wide")

st.title("🌍 African Climate Trends Analysis Dashboard")
st.markdown("**Data:** NASA POWER (2015-2026) | **Countries:** Ethiopia, Kenya, Nigeria, Sudan, Tanzania")

@st.cache_data
def load_all_data():
    data_dir = Path(__file__).parent.parent / "data"
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    country_names = ['Ethiopia', 'Kenya', 'Nigeria', 'Sudan', 'Tanzania']
    all_data = {}
    
    for country in countries:
        file_path = data_dir / f"{country}.csv"
        if file_path.exists():
            df = pd.read_csv(file_path)
            # Clean data
            df.replace(-999, np.nan, inplace=True)
            df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format="%Y%j")
            df['Year'] = df['Date'].dt.year
            # Forward fill
            weather_cols = ['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M']
            for col in weather_cols:
                if col in df.columns:
                    df[col] = df[col].fillna(method='ffill')
            all_data[country] = df
        else:
            st.warning(f"File not found: {file_path}")
    
    return all_data

with st.spinner("Loading data..."):
    all_data = load_all_data()

if not all_data:
    st.error("No data loaded. Please ensure CSV files are in the 'data/' folder.")
    st.stop()

# Sidebar
st.sidebar.header("Filters")

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    ['Ethiopia', 'Kenya', 'Nigeria', 'Sudan', 'Tanzania'],
    default=['Ethiopia']
)

# Get year range from data
all_years = []
for df in all_data.values():
    all_years.extend(df['Year'].unique())
min_year, max_year = min(all_years), max(all_years)

year_range = st.sidebar.slider("Year Range", min_year, max_year, (min_year, max_year))

variable = st.sidebar.selectbox(
    "Select Variable",
    ['T2M', 'PRECTOTCORR', 'RH2M'],
    format_func=lambda x: {'T2M': 'Temperature (°C)', 'PRECTOTCORR': 'Precipitation (mm)', 'RH2M': 'Humidity (%)'}[x]
)

# Filter data
df_list = []
for country in selected_countries:
    key = country.lower()
    if key in all_data:
        df = all_data[key]
        mask = (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])
        temp_df = df[mask].copy()
        temp_df['Country'] = country
        df_list.append(temp_df)

if df_list:
    df_combined = pd.concat(df_list, ignore_index=True)
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Countries", len(selected_countries))
    col2.metric("Years", f"{year_range[0]}-{year_range[1]}")
    col3.metric(f"Avg {variable}", f"{df_combined[variable].mean():.1f}")
    
    # Line chart
    st.subheader(f"{variable} Trends")
    fig, ax = plt.subplots(figsize=(12, 5))
    for country in selected_countries:
        country_df = df_combined[df_combined['Country'] == country]
        monthly = country_df.groupby(country_df['Date'].dt.to_period('M'))[variable].mean()
        ax.plot(monthly.index.astype(str), monthly.values, label=country, linewidth=1.5)
    ax.set_xlabel("Date")
    ax.set_ylabel(variable)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Boxplot
    st.subheader("Distribution by Country")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    data_to_plot = [df_combined[df_combined['Country'] == c][variable].dropna() for c in selected_countries]
    ax2.boxplot(data_to_plot, labels=selected_countries, patch_artist=True)
    ax2.set_ylabel(variable)
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)
    
    # Summary
    st.subheader("Summary Statistics")
    st.dataframe(df_combined.groupby('Country')[variable].agg(['mean', 'median', 'std']).round(2))
else:
    st.warning("No data for selected filters")