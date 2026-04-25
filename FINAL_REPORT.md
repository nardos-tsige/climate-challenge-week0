# African Climate Trend Analysis for COP32
## 10 Academy Week 0 Final Report

**Author:** Nardos T. | **Date:** April 28, 2026
**Dashboard:** [Click Here](https://climate-challenge-week0-cf86fc3wurgfhpdreq3zp7.streamlit.app/)

---

## Executive Summary

Analyzed climate data (2015-2026) for Ethiopia, Kenya, Nigeria, Sudan, and Tanzania using NASA POWER data.

**Key Findings:**
- **Sudan** is most vulnerable (38°C max temp, 72.7% dry days)
- **Ethiopia** is coolest (16.1°C mean - highland advantage)
- **Nigeria** has highest flood risk (166mm max rain)
- Temperature differences are statistically significant (p < 0.001)

---

## Task 1: Environment Setup

- GitHub repo: `climate-challenge-week0`
- Branches: `setup-task`, `eda-ethiopia`, `compare-countries`, `dashboard-dev`
- Python venv with pandas, numpy, matplotlib, seaborn, streamlit
- GitHub Actions CI/CD workflow
- 3+ conventional commits merged via PR

---

## Task 2: Data Cleaning & EDA

**Cleaning Steps:**
1. Added Country column
2. Converted YEAR+DOY to Date
3. Replaced -999 with NaN
4. Forward-fill for missing values
5. Retained outliers (climate extremes are real)

**Key Visualizations:**
- Monthly temperature trends (warmest/coolest annotated)
- Monthly precipitation (peak rainy season)
- Correlation heatmap
- Distribution plots (log scale)

**Cleaned data saved to** `data/*_clean.csv`

---

## Task 3: Cross-Country Results

**Temperature Summary:**

| Country | Mean Temp | Dry Days |
|---------|-----------|----------|
| Ethiopia | 16.1°C | 20.7% |
| Kenya | 20.4°C | 6.3% |
| Nigeria | 26.7°C | 11.8% |
| Sudan | 28.8°C | 72.7% |
| Tanzania | 26.8°C | 5.2% |

**Precipitation Summary:**

| Country | Mean Rain | Max Rain |
|---------|-----------|----------|
| Ethiopia | 3.6 mm/day | 82 mm |
| Kenya | 1.5 mm/day | 52 mm |
| Nigeria | 4.2 mm/day | 166 mm |
| Sudan | 0.6 mm/day | 67 mm |
| Tanzania | 3.7 mm/day | 123 mm |

**Statistical Test:** ANOVA p < 0.001 → differences are real

**Vulnerability Ranking (1=most vulnerable):**
1. Sudan (heat + drought)
2. Nigeria (flood risk)
3. Ethiopia (variable)
4. Tanzania (moderate)
5. Kenya (most balanced)

---

## Bonus: Interactive Dashboard

**Features:**
- Country multi-select
- Year slider (2015-2026)
- Variable selector (Temp/Precip/Humidity)
- Line chart & boxplot
- Download data as CSV

**Screenshots:** `dashboard_screenshots/` folder

**Live:** [Streamlit App](https://climate-challenge-week0-cf86fc3wurgfhpdreq3zp7.streamlit.app/)

---

## COP32 Recommendations

| Priority | Action | Target |
|----------|--------|--------|
| 1 | Climate finance | Sudan |
| 2 | Heat warning systems | All countries |
| 3 | Flood defense | Nigeria |
| 4 | Drought agriculture | Ethiopia, Sudan |
| 5 | Water infrastructure | Regional |

---

## Conclusion

Sudan needs priority climate finance. Ethiopia's highland gives it a cooler profile but regional cooperation is key. The data provides strong evidence for action at COP32.

---

**Repository:** https://github.com/nardos-tsige/climate-challenge-week0
