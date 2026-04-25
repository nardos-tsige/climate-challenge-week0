# Climate Change Analysis Dashboard

## Interactive Climate Dashboard for East Africa

This dashboard provides interactive visualizations for climate data analysis across five East African countries.

### Features

- **Country Multi-Selector**: Compare multiple countries simultaneously
- **Year Range Slider**: Zoom into specific time periods (2015-2026)
- **Variable Selector**: Toggle between Temperature and Precipitation views
- **Interactive Visualizations**: Hover, zoom, and pan capabilities
- **Statistical Summary**: Real-time statistics based on filters
- **Data Export**: Download filtered data as CSV

### Countries Included
- Ethiopia
- Kenya  
- Nigeria
- Sudan
- Tanzania

### Variables
- **T2M**: Temperature at 2 meters (°C)
- **PRECTOTCORR**: Corrected Precipitation (mm/day)

### Installation

1. Clone the repository:
   git clone <your-repo-url>
   cd climate-challenge-week0

2. Install dependencies:
    pip install -r requirements.txt

3. Run the dashboard:
    streamlit run app/main.py

**Deployment on Streamlit Cloud**
1. Push your code to GitHub

2. Go to share.streamlit.io

3. Connect your GitHub repository

4. Set:

    - Main file path: app/main.py

    - Python version: 3.9

5. Click Deploy

**Development Process**
- Branch: dashboard-dev

- Initial commit: "feat: basic Streamlit UI with interactive widgets"

- Added features: country selector, year slider, variable selector

- Implemented caching for performance

- Added professional styling and layout

**Usage Instructions**
1. Select Countries: Use the sidebar to choose countries to analyze

2. Adjust Year Range: Slide to focus on specific years

3. Choose Variable: Toggle between temperature and precipitation

4. Explore Charts: Hover for details, zoom for closer inspection

5. Download Data: Export filtered data for further analysis

**Dashboard Structure**
├── app/
│   ├── __init__.py
│   ├── main.py       # Main Streamlit application
│   └── utils.py      # Utility functions (optional)
├── data/             # CSV files (git ignored)
├── scripts/          # Supporting scripts
├── requirements.txt  # Python dependencies
└── README.md        # Documentation
**Troubleshooting**
- Issue: "No data found"
- Solution: Ensure CSV files are in the data/ folder with correct names (e.g., ethiopia_clean.csv)

- Issue: Dashboard not loading
- Solution: Run pip install -r requirements.txt to install dependencies

Live Demo
----

### Author

**Nardos T.**  
Climate Challenge Week 0 Participant

**License**
MIT

## **Step 8: Test Locally**

In your terminal:
    streamlit run app/main.py