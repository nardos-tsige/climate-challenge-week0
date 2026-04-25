# Week 0 Challenge - Interim Report

## Task 1: Git & Environment Setup

### Summary
- Created GitHub repository: `climate-challenge-week0`
- Set up Python virtual environment (venv)
- Created branch `setup-task` with 3 conventional commits:
  - `init: add .gitignore`
  - `chore: venv setup`
  - `ci: add GitHub Actions workflow`
- Added GitHub Actions CI/CD pipeline
- Merged via Pull Request to `main`

### Repository Structure

climate-challenge-week0/
├── .github/workflows/ci.yml
├── .gitignore
├── requirements.txt
├── README.md
└── src/


### KPI Status
-  Dev environment documented
-  CI workflow passes on push to main
-  3+ commits merged via PR

---

## Task 2: Data Profiling, Cleaning & EDA

### Approach

**Data Loading & Cleaning:**
- Loaded CSV files for 5 countries (Ethiopia, Kenya, Nigeria, Sudan, Tanzania)
- Added Country column
- Converted YEAR+DOY to datetime
- Replaced -999 sentinel values with NaN
- Applied forward-fill for missing weather data

**Outlier Detection:**
- Computed Z-scores for key climate variables
- Retained outliers (real climate extremes are meaningful)
- Documented reasoning in markdown

**EDA Visualizations Produced:**
- Monthly temperature trends (2015-2026)
- Monthly precipitation patterns
- Correlation heatmaps
- Precipitation distribution (log scale)
- Bubble charts (temp vs humidity, size=rainfall)

**Clean Data Export:**
- Saved cleaned CSVs to `data/` folder
- Excluded from Git per challenge instructions

### Sample Findings
- Sudan warmest (28.8°C mean), Ethiopia coolest (16.1°C mean)
- Sudan has 72.7% dry days vs Tanzania 5.2%
- Nigeria shows extreme rainfall variability (max 166.1 mm/day)

### KPI Status
-  NASA header and -999 handled
-  Cleaned CSVs exported
-  Time series, correlation, distribution plots completed
-  Written interpretations for each visualization

---

## Dashboard Progress (Bonus)

- Streamlit dashboard created with:
  - Country multi-select widget
  - Year range slider (2015-2026)
  - Variable selector (Temperature/Precipitation/Humidity)
  - Interactive line charts and boxplots
  - Summary statistics table
  - Data download functionality
-  Deployed to Streamlit Cloud
-  Screenshots added to repository

---

## Issues Encountered & Solutions

| Issue | Solution |
|-------|----------|
| Python 3.13 compatibility | Used Python 3.11 for package compatibility |
| Git lock file error | Deleted `.git/index.lock` |
| CSV files not pushing | Updated `.gitignore` to allow CSV files |
| Streamlit deployment | Used `ffill()` instead of `fillna(method='ffill')` |

---

## Next Steps (Task 3)

- Cross-country comparison analysis
- Statistical testing (ANOVA)
- Climate vulnerability ranking
- COP32 policy recommendations

---

## Repository Links

- GitHub: https://github.com/nardos-tsige/climate-challenge-week0
- Dashboard (if deployed): [Streamlit App](https://climate-challenge-week0-cf86fc3wurgfhpdreq3zp7.streamlit.app/)
