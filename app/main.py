# app/main.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))

# Page configuration
st.set_page_config(
    page_title="Climate Dashboard - East Africa",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: semi-bold;
        color: #2c3e50;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load data function with caching
@st.cache_data
def load_all_data():
    """Load all country data"""
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    all_data = []
    
    for country in countries:
        file_path = Path(f'data/{country}_clean.csv')
        if file_path.exists():
            df = pd.read_csv(file_path)
            df['Date'] = pd.to_datetime(df['Date'])
            df['Country'] = country.capitalize()
            df['Year'] = df['Date'].dt.year
            df['Month'] = df['Date'].dt.month
            all_data.append(df)
    
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    return pd.DataFrame()

# Title
st.markdown('<div class="main-header">🌍 East Africa Climate Dashboard</div>', unsafe_allow_html=True)
st.markdown("### Interactive Climate Data Explorer for Ethiopia, Kenya, Nigeria, Sudan, and Tanzania")

# Load data
with st.spinner("Loading climate data..."):
    df = load_all_data()

if df.empty:
    st.error("❌ No data found! Please ensure CSV files are in the 'data/' folder.")
    st.stop()

# Sidebar filters
st.sidebar.markdown("## 🔍 Filters")

# Country selector
countries = st.sidebar.multiselect(
    "Select Countries",
    options=df['Country'].unique(),
    default=df['Country'].unique()[:3],
    help="Choose one or more countries to analyze"
)

# Year range slider
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

# Variable selector
variable = st.sidebar.selectbox(
    "Select Variable",
    options=['T2M', 'PRECTOTCORR'],
    format_func=lambda x: 'Temperature (°C)' if x == 'T2M' else 'Precipitation (mm/day)'
)

# Filter data based on selections
filtered_df = df[df['Country'].isin(countries)]
filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & 
                          (filtered_df['Year'] <= year_range[1])]

# Display KPIs
st.markdown("## 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Countries Selected", len(countries))

with col2:
    avg_temp = filtered_df['T2M'].mean()
    st.metric("Avg Temperature", f"{avg_temp:.1f}°C")

with col3:
    avg_rain = filtered_df['PRECTOTCORR'].mean()
    st.metric("Avg Precipitation", f"{avg_rain:.2f} mm/day")

with col4:
    data_range = f"{year_range[0]} - {year_range[1]}"
    st.metric("Time Period", data_range)

# Main visualizations
st.markdown("## 📈 Climate Trends")

# Temperature trend line chart
if variable == 'T2M':
    fig1 = px.line(
        filtered_df,
        x='Date',
        y='T2M',
        color='Country',
        title='Temperature Trends Over Time',
        labels={'T2M': 'Temperature (°C)', 'Date': 'Date'},
        template='plotly_white'
    )
    fig1.update_layout(
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Add monthly average heatmap
    st.markdown("### 🌡️ Monthly Average Temperature Patterns")
    monthly_temp = filtered_df.groupby(['Country', 'Month'])['T2M'].mean().reset_index()
    fig_heatmap = px.density_heatmap(
        monthly_temp,
        x='Month',
        y='Country',
        z='T2M',
        title='Monthly Temperature Patterns',
        labels={'T2M': 'Temperature (°C)', 'Month': 'Month', 'Country': ''},
        color_continuous_scale='Reds',
        template='plotly_white'
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

else:
    fig1 = px.line(
        filtered_df,
        x='Date',
        y='PRECTOTCORR',
        color='Country',
        title='Precipitation Trends Over Time',
        labels={'PRECTOTCORR': 'Precipitation (mm/day)', 'Date': 'Date'},
        template='plotly_white'
    )
    fig1.update_layout(
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Boxplot for precipitation distribution
    st.markdown("### 💧 Precipitation Distribution")
    fig_box = px.box(
        filtered_df,
        x='Country',
        y='PRECTOTCORR',
        color='Country',
        title='Precipitation Distribution by Country',
        labels={'PRECTOTCORR': 'Precipitation (mm/day)', 'Country': ''},
        template='plotly_white'
    )
    fig_box.update_layout(showlegend=False)
    st.plotly_chart(fig_box, use_container_width=True)

# Additional statistics
st.markdown("## 📊 Statistical Summary")

# Create summary statistics
summary_stats = filtered_df.groupby('Country').agg({
    'T2M': ['mean', 'std', 'min', 'max'],
    'PRECTOTCORR': ['mean', 'std', 'max']
}).round(2)

summary_stats.columns = ['Temp Mean', 'Temp Std', 'Temp Min', 'Temp Max', 
                         'Rain Mean', 'Rain Std', 'Rain Max']

st.dataframe(summary_stats, use_container_width=True)

# Download button for filtered data
st.markdown("## 💾 Download Data")
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="📥 Download filtered data as CSV",
    data=csv,
    file_name="climate_data_filtered.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    Dashboard created by <strong>Nardos T.</strong> | Climate Challenge Week 0<br>
    Data source: Climate API (2015-2026)
    </div>
    """,
    unsafe_allow_html=True
)