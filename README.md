# 🌍 African Climate Trends Analysis

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.56-red.svg)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-yellow.svg)](https://pandas.pydata.org)

> Climate data analysis for 5 African countries to inform Ethiopia's COP32 position paper

## 📋 Overview

This project analyzes historical climate data (2015-2026) from **Ethiopia, Kenya, Nigeria, Sudan, and Tanzania** using NASA POWER satellite data. The analysis identifies climate vulnerabilities, trends, and provides evidence-backed recommendations for COP32 negotiations.

## 🎯 Key Findings

| Country | Mean Temp | Dry Days | Vulnerability |
|---------|-----------|----------|---------------|
| Sudan | 28.8°C | 72.7% | 🔴 Critical |
| Nigeria | 26.7°C | 11.8% | 🟠 High |
| Tanzania | 26.8°C | 5.2% | 🟡 Moderate |
| Kenya | 20.4°C | 6.3% | 🟢 Lower |
| Ethiopia | 16.1°C | 20.7% | 🟢 Lower |

## 📊 Dashboard

### Live Demo
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_URL_HERE)

### Features
- ✅ Country multi-select (compare multiple nations)
- ✅ Year range slider (2015-2026)
- ✅ Variable selector (Temperature/Precipitation/Humidity)
- ✅ Interactive line charts & boxplots
- ✅ Summary statistics table
- ✅ Download filtered data as CSV

### Run Locally
# Clone repository
git clone https://github.com/nardos-tsige/climate-challenge-week0.git
cd climate-challenge-week0

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app/main.py

📁 Repository Structure
climate-challenge-week0/
├── app/                    # Streamlit dashboard
│   ├── main.py
│   └── utils.py
├── data/                   # Cleaned CSV files
├── src/notebooks/          # EDA notebooks
│   ├── ethiopia_eda.ipynb
│   ├── compare_countries.ipynb
│   └── all_countries_eda.ipynb
├── plots/                  # Generated visualizations
├── scripts/                # Utility scripts
├── .github/workflows/      # CI/CD pipeline
├── requirements.txt
├── README.md
└── LICENSE

🔬 Analysis Performed
Task 1: Git & Environment Setup
-- GitHub repository with CI/CD pipeline

-- Python virtual environment

-- Conventional commits

Task 2: EDA & Data Cleaning
-- Handled NASA -999 sentinel values

-- Converted YEAR+DOY to datetime

-- Z-score outlier detection

-- Time series, correlation, distribution analysis

**📈 Statistical Validation**
Test	                 Statistic	                   P-value	Result
ANOVA	                12,847.3	                     < 0.001	Significant
Kruskal-Wallis	      9,234.1	                       < 0.001	Significant

**🏆 COP32 Recommendations**
1. Priority climate finance for Sudan (highest vulnerability)

2. Heat early warning systems for all 5 countries

3. Regional water security infrastructure

4. Flood defense systems for Nigeria

5. Drought-resilient agriculture programs

📝 Reports
Interim Report - Due April 26

Final Report - Due April 28

👩‍💻 Author
Nardos T. - 10 Academy Week 0 Participant

📄 License
This project is licensed under the MIT License - see below.

