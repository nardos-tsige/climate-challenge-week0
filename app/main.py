import streamlit as st
import pandas as pd
from pathlib import Path

st.title("TEST DASHBOARD")

# Check if files exist
data_dir = Path(__file__).parent.parent / "data"

st.write(f"Looking for data in: {data_dir}")
st.write(f"Does folder exist? {data_dir.exists()}")

if data_dir.exists():
    files = list(data_dir.glob("*.csv"))
    st.write(f"Found {len(files)} CSV files:")
    for f in files:
        st.write(f"  - {f.name}")
        
        # Try to read first file
        if "ethiopia" in f.name.lower():
            df = pd.read_csv(f)
            st.write(f"Columns: {list(df.columns)}")
            st.dataframe(df.head())
else:
    st.error(f"Data folder not found at {data_dir}")