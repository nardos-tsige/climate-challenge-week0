# app/main.py - Fully Functional Dashboard

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Page config
st.set_page_config(page_title="African Climate Dashboard", layout="wide")

st.title("🌍 African Climate Trends Analysis Dashboard")
st.markdown("**Data:** NASA POWER (2015-2026) | **Countries:** Ethiopia, Kenya, Nigeria, Sudan, Tanzania")

@st.cache_data
def load_and_clean_data():
    """Load and clean all country data"""
    data_dir = Path(__file__).parent.parent / "data"
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    all_data = {}
    
    for country in countries:
        file_path = data_dir / f"{country}.csv"
        if file_path.exists():
            df = pd.read_csv(file_path)
            
            # Replace -999 with NaN
            df.replace(-999, np.nan, inplace=True)
            
            # Create Date column from YEAR and DOY
            df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format="%Y%j")
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.month
            
            # Forward fill missing values (corrected method)
            weather_cols = ['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M']
            for col in weather_cols:
                if col in df.columns:
                    df[col] = df[col].fillna(method='ffill')
            
            all_data[country.capitalize()] = df
            print(f"✅ Loaded {country}: {len(df)} rows")
        else:
            st.warning(f"File not found: {file_path}")
    
    return all_data

# Load data
with st.spinner("Loading climate data..."):
    try:
        all_data = load_and_clean_data()
        if not all_data:
            st.error("No data loaded. Please check CSV files in 'data/' folder.")
            st.stop()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

# Sidebar Filters
st.sidebar.header("🔍 Filters")

country_names = list(all_data.keys())
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    country_names,
    default=['Ethiopia'] if 'Ethiopia' in country_names else country_names[:1]
)

# Get year range from all data
all_years = []
for df in all_data.values():
    all_years.extend(df['Year'].tolist())
min_year = int(min(all_years))
max_year = int(max(all_years))

year_range = st.sidebar.slider(
    "Select Year Range",
    min_year, max_year,
    (min_year, max_year)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ['T2M', 'PRECTOTCORR', 'RH2M'],
    format_func=lambda x: {
        'T2M': '🌡️ Temperature (°C)',
        'PRECTOTCORR': '💧 Precipitation (mm)',
        'RH2M': '💨 Humidity (%)'
    }[x]
)

# Filter data based on selections
filtered_data = []
for country in selected_countries:
    if country in all_data:
        df = all_data[country]
        mask = (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])
        temp_df = df[mask].copy()
        if not temp_df.empty:
            temp_df['Country'] = country
            filtered_data.append(temp_df)

# Display dashboard
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
        if not country_df.empty:
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
    
    data_to_plot = []
    plot_labels = []
    for country in selected_countries:
        country_df = df_combined[df_combined['Country'] == country]
        if not country_df.empty:
            data_to_plot.append(country_df[variable].dropna())
            plot_labels.append(country)
    
    if data_to_plot:
        bp = ax2.boxplot(data_to_plot, labels=plot_labels, patch_artist=True)
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        for i, patch in enumerate(bp['boxes']):
            if i < len(colors):
                patch.set_facecolor(colors[i])
    
    ax2.set_ylabel(variable)
    ax2.set_title(f'Distribution of {variable} by Country')
    ax2.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig2)
    
    # Summary Statistics
    st.subheader("📋 Summary Statistics")
    summary = df_combined.groupby('Country')[variable].agg(['mean', 'median', 'std', 'min', 'max']).round(2)
    st.dataframe(summary, use_container_width=True)
    
    # Download button
    csv_data = df_combined.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_data,
        file_name=f"climate_data_{year_range[0]}_{year_range[1]}.csv",
        mime="text/csv"
    )
    
    # Raw data expander
    with st.expander("📊 View Raw Data"):
        st.dataframe(df_combined, use_container_width=True)
        
else:
    st.warning("No data available for selected filters. Please adjust your selection.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 20px;'>
    <p>🌍 Data Source: NASA POWER (Prediction of Worldwide Energy Resources) | 2015-2026</p>
    <p>📊 10 Academy Week 0 Challenge - African Climate Trend Analysis for COP32</p>
    </div>
    """,
    unsafe_allow_html=True
)