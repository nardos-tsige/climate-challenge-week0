# app/main.py - Complete Working Dashboard

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="African Climate Dashboard", layout="wide")

st.title("🌍 African Climate Trends Analysis Dashboard")
st.markdown("**Data:** NASA POWER (2015-2026) | **Countries:** Ethiopia, Kenya, Nigeria, Sudan, Tanzania")

@st.cache_data
def load_and_clean_data():
    data_dir = Path(__file__).parent.parent / "data"
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    all_data = {}
    
    for country in countries:
        file_path = data_dir / f"{country}.csv"
        if file_path.exists():
            df = pd.read_csv(file_path)
            
            # Clean the data
            df.replace(-999, np.nan, inplace=True)
            
            # Create Date column
            df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format="%Y%j")
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.month
            
            # Forward fill missing values
            weather_cols = ['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M']
            for col in weather_cols:
                if col in df.columns:
                    df[col] = df[col].fillna(method='ffill')
            
            all_data[country.capitalize()] = df
    
    return all_data

with st.spinner("Loading climate data..."):
    all_data = load_and_clean_data()

if not all_data:
    st.error("No data loaded. Please check CSV files.")
    st.stop()

# Sidebar Filters
st.sidebar.header("🔍 Filters")

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    list(all_data.keys()),
    default=['Ethiopia']
)

# Get year range
all_years = []
for df in all_data.values():
    all_years.extend(df['Year'].unique())
min_year, max_year = int(min(all_years)), int(max(all_years))

year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

variable = st.sidebar.selectbox(
    "Select Variable",
    ['T2M', 'PRECTOTCORR', 'RH2M'],
    format_func=lambda x: {
        'T2M': '🌡️ Temperature (°C)', 
        'PRECTOTCORR': '💧 Precipitation (mm)', 
        'RH2M': '💨 Humidity (%)'
    }[x]
)

# Filter data
filtered_data = []
for country in selected_countries:
    df = all_data[country]
    mask = (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])
    temp_df = df[mask].copy()
    temp_df['Country'] = country
    filtered_data.append(temp_df)

if filtered_data:
    df_combined = pd.concat(filtered_data, ignore_index=True)
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("📊 Countries", len(selected_countries))
    col2.metric("📅 Years", f"{year_range[0]}-{year_range[1]}")
    col3.metric(f"📈 Average", f"{df_combined[variable].mean():.1f}")
    
    st.markdown("---")
    
    # Line Chart
    st.subheader(f"📈 {variable} Trends Over Time")
    fig, ax = plt.subplots(figsize=(12, 5))
    
    for country in selected_countries:
        country_df = df_combined[df_combined['Country'] == country]
        monthly = country_df.groupby(country_df['Date'].dt.to_period('M'))[variable].mean()
        ax.plot(monthly.index.astype(str), monthly.values, label=country, linewidth=1.5)
    
    ax.set_xlabel("Date")
    ax.set_ylabel(variable)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)
    
    # Boxplot
    st.subheader("📊 Distribution by Country")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    data_to_plot = [df_combined[df_combined['Country'] == c][variable].dropna() for c in selected_countries]
    bp = ax2.boxplot(data_to_plot, labels=selected_countries, patch_artist=True)
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    for i, patch in enumerate(bp['boxes']):
        if i < len(colors):
            patch.set_facecolor(colors[i])
    
    ax2.set_ylabel(variable)
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig2)
    
    # Summary Statistics
    st.subheader("📋 Summary Statistics")
    summary = df_combined.groupby('Country')[variable].agg(['mean', 'median', 'std']).round(2)
    st.dataframe(summary, use_container_width=True)
    
    # Download button
    csv = df_combined.to_csv(index=False).encode()
    st.download_button("📥 Download Filtered Data", csv, "climate_data.csv", "text/csv")
    
else:
    st.warning("No data available for selected filters.")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>🌍 Data from NASA POWER (2015-2026) | 10 Academy Week 0 Challenge</div>",
    unsafe_allow_html=True
)