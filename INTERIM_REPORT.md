**Week 0 Challenge – Interim Report**

**African Climate Trend Analysis: Supporting COP32 Negotiations with Data-Driven Insights**

Prepared for: EthioClimate Analytics
Project Focus: Evidence-based policy recommendations for COP32
Reporting Period: Week 0 Interim
Date: 4/27/2026


1. Executive Summary

This interim report documents the foundational work completed during Week 0 of the African Climate Trend Analysis challenge. The objective is to establish a reproducible data pipeline, profile and clean climate datasets for five African nations (Ethiopia, Kenya, Nigeria, Sudan, Tanzania), and generate initial exploratory insights. This work directly supports EthioClimate Analytics' mandate to provide evidence-based policy recommendations for the upcoming COP32 negotiations, with a focus on climate vulnerability, adaptation strategies, and cross-country resource allocation.

The three-layer analytical framework guiding this work is:

| Layer | Focus | Status |
|-------|-------|--------|
| Layer 1 | Data Engineering & Environment Setup | Complete |
| Layer 2 | Exploratory Data Analysis & Profiling | Complete |
| Layer 3 | Policy-Driven Insights & Recommendations | In Progress (Task 3) |


2. Business Context & Project Objective

2.1 The Problem

African nations face disproportionate climate impacts despite minimal historical emissions. At COP32, evidence-based arguments for climate financing, technology transfer, and adaptation support will be critical. However, raw climate data is messy, incomplete, and requires rigorous cleaning and analysis to be actionable.

2.2 Our Role

As climate data analysts at EthioClimate Analytics, we are preparing a comprehensive climate trend analysis covering five East and West African nations. Our work will directly inform:
- National adaptation planning
- COP32 negotiation briefs
- Climate vulnerability rankings
- Regional cooperation frameworks

2.3 The Three-Layer Framework

To ensure rigorous, policy-relevant outputs, we structured our work into three interconnected layers:

Layer 1: Data Engineering & Environment Setup
- Reproducible GitHub repository
- CI/CD pipeline for quality control
- Virtual environment for dependency management

Layer 2: Exploratory Data Analysis (EDA)
- Data profiling and cleaning
- Handling NASA sentinel values (-999)
- Visualizing trends, distributions, and anomalies

Layer 3: Policy-Driven Insights
- Cross-country statistical comparisons
- Climate vulnerability ranking
- COP32 policy recommendations (Task 3)

2.4 Success KPIs

| KPI | Target | Status |
|-----|--------|--------|
| GitHub with CI/CD | Established | Yes |
| 3+ conventional commits merged via PR | Complete | Yes |
| Cleaned CSVs for 5 countries | Exported | Yes |
| NASA header & -999 handled | Complete | Yes |
| Time series, correlation, distribution plots | Completed | Yes |
| Written interpretations for each viz | Completed | Yes |
| Streamlit dashboard (bonus) | Deployed | Yes |


3. Task 1: Git & Environment Setup

3.1 Summary of Deliverables

| Activity | Details |
|----------|---------|
| Repository | climate-challenge-week0 |
| Virtual Environment | Python venv (Python 3.11) |
| Feature Branch | setup-task |
| Conventional Commits | init: add .gitignore / chore: venv setup / ci: add GitHub Actions |
| CI/CD | GitHub Actions workflow (runs on push to main) |
| Merge Strategy | Pull Request reviewed and merged |

3.2 Repository Structure

climate-challenge-week0/
├── .github/workflows/
│   └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
└── src/

3.3 CI/CD Pipeline Functionality

The GitHub Actions workflow automatically:
- Sets up Python 3.11
- Installs dependencies from requirements.txt
- Runs linting and basic validation
- Triggers on every push to main branch

3.4 KPI Verification

- Development environment documented in README
- CI workflow passes on all pushes to main
- 3+ conventional commits merged via pull request


4. Task 2: Data Profiling, Cleaning & EDA

4.1 Data Sources

Raw data obtained from NASA Earth Observatory (MODIS and TRMM satellites) covering:
- Ethiopia
- Kenya
- Nigeria
- Sudan
- Tanzania
- Time period: 2015–2026 (daily resolution)

4.2 Data Cleaning Approach

| Step | Method | Rationale |
|------|--------|-----------|
| Add country identifier | New Country column | Enables cross-country analysis |
| Parse dates | Convert YEAR + DOY to datetime | Enables time series operations |
| Handle missing values | Forward-fill (ffill) | Preserves temporal continuity |
| Sentinel values | Replace -999 with NaN | NASA convention for missing/error |
| Outlier handling | Z-score calculation (retained) | Climate extremes are real, not errors |

4.3 Handling of NASA Sentinel Values

The -999 values in the raw data represent sensor errors or missing observations. These were converted to NaN and then forward-filled using temporal proximity, which is appropriate for climate variables where adjacent days are highly correlated.

4.4 Outlier Documentation

Z-scores were computed for temperature, precipitation, and humidity. Outliers were retained because:
- Climate extremes (heatwaves, floods, droughts) are scientifically meaningful
- Removing outliers would underestimate climate risk
- Policy recommendations require understanding of extreme events

4.5 EDA Visualizations Produced

| Visualization | Purpose | Key Insight |
|---------------|---------|--------------|
| Monthly temperature trends (2015–2026) | Detect warming patterns | All countries show warming, Sudan highest |
| Monthly precipitation patterns | Identify wet/dry seasons | Strong West African monsoon influence |
| Correlation heatmaps | Understand variable relationships | Temp-humidity negative in Sahel |
| Precipitation distribution (log scale) | Handle skewed rainfall data | Most days dry or light rain |
| Bubble charts (temp vs humidity, size=rainfall) | Multivariate exploration | High rainfall correlates with cooler temps |

4.6 Sample Findings (Initial)

| Finding | Data Support |
|---------|---------------|
| Sudan is warmest (28.8°C mean) vs Ethiopia coolest (16.1°C mean) | Temperature means by country |
| Sudan has 72.7% dry days vs Tanzania 5.2% | Precipitation frequency analysis |
| Nigeria shows extreme rainfall variability (max 166.1 mm/day) | Daily rainfall distribution |

4.7 Clean Data Export

Cleaned CSVs saved to data/ folder and excluded from Git per challenge instructions (handled via .gitignore). Each file contains:
- Standardized column names
- No -999 sentinel values
- Forward-filled missing data
- Added Country and proper Date columns

4.8 Written Interpretations

Each visualization is accompanied by:
- Observed pattern description
- Potential climate driver
- Policy implication for COP32


5. Dashboard Progress (Bonus)

A fully interactive Streamlit dashboard has been deployed with the following features:

| Feature | Implementation Status |
|---------|----------------------|
| Country multi-select widget | Complete |
| Year range slider (2015–2026) | Complete |
| Variable selector (Temp/Precip/Humidity) | Complete |
| Interactive line charts | Complete |
| Boxplots by month | Complete |
| Summary statistics table | Complete |
| Data download (CSV) | Complete |
| Deployment to Streamlit Cloud | Complete |
| Screenshots in repository | Complete |

Dashboard Link: [Streamlit App](https://climate-challenge-week0-cf86fc3wurgfhpdreq3zp7.streamlit.app/) 


6. Issues Encountered & Resolutions

| Issue | Root Cause | Solution Applied |
|-------|------------|------------------|
| Python 3.13 compatibility | Package dependencies not updated | Downgraded to Python 3.11 |
| Git lock file error | Previous process interruption | Deleted .git/index.lock |
| CSV files not pushing | .gitignore blocking /data | Updated .gitignore to allow CSV exports |
| Streamlit deployment error | fillna(method='ffill') deprecated | Replaced with .ffill() |


7. Next Steps: Task 3 (Policy Layer)

The following analyses are planned to complete the three-layer framework:

| Activity | Method | Policy Relevance |
|----------|--------|------------------|
| Cross-country comparison | Multi-country statistical summary | Regional vulnerability ranking |
| Statistical testing | ANOVA across nations | Determine if climate differences are significant |
| Climate vulnerability ranking | Composite index (temp + rainfall variability) | Targeting of adaptation funds |
| COP32 policy recommendations | Evidence synthesis | Negotiation briefs for African delegations |


8. Repository & Access

| Resource | URL |
|----------|-----|
| GitHub Repository | https://github.com/nardos-tsige/climate-challenge-week0 |
| Streamlit Dashboard | [Streamlit App](https://climate-challenge-week0-cf86fc3wurgfhpdreq3zp7.streamlit.app/) 
| Cleaned Data (excluded from Git) | Available upon request |


9. Conclusion

Week 0 deliverables successfully established a reproducible data pipeline and generated initial climate insights for five African nations. The work directly supports EthioClimate Analytics' preparation for COP32 by:

1. Creating a version-controlled, CI/CD-enabled codebase
2. Cleaning and profiling NASA climate data with transparent handling of sentinel values
3. Producing visualizations and interpretations that reveal meaningful cross-country patterns
4. Deploying an interactive dashboard for stakeholder exploration

The three-layer framework ensures that technical rigor translates directly to policy relevance. Task 3 will complete this framework with statistical comparisons and actionable COP32 recommendations.



