**African Climate Trend Analysis for COP32**

**10 Academy Week 0 Final Report**

1. Introduction & Business Context

1.1 The Problem

African nations are disproportionately vulnerable to climate change despite contributing the least to global emissions. Policymakers at COP32 (the 2026 UN Climate Change Conference) require actionable, data-driven evidence to allocate climate finance, design adaptation strategies, and prioritize interventions across countries with vastly different climate profiles.

1.2 EthioClimate Analytics & My Role

This project was commissioned by EthioClimate Analytics, a regional climate intelligence firm advising the African Union and COP32 negotiators. As a Climate Data Analyst, my responsibility was to:
- Analyze historical climate trends (2015–2026) for five key African nations
- Identify statistically significant differences and vulnerability rankings
- Deliver an interactive dashboard for exploration by COP32 delegates

1.3 The Three-Layer Analytical Framework

To ensure rigor and policy relevance, I structured my work around three layers:

| Layer | Focus | Deliverable |
|-------|-------|-------------|
| Layer 1: Environment & Reproducibility | Git, CI/CD, python venv | GitHub repo with branches, PRs, Actions |
| Layer 2: Data Cleaning & EDA | Missing values, outliers, visualizations | Clean datasets, correlation plots |
| Layer 3: Cross-Country Analysis | Statistical testing, vulnerability ranking, dashboard | ANOVA results, ranking table, interactive Streamlit app |

1.4 Target Audience

- COP32 climate finance negotiators
- National adaptation planners (Ethiopia, Kenya, Nigeria, Sudan, Tanzania)
- EthioClimate Analytics leadership and partners


2. Executive Summary

Analyzed climate data (2015–2026) for Ethiopia, Kenya, Nigeria, Sudan, and Tanzania using NASA POWER data.

Key Findings:
- Sudan is most vulnerable (38°C max temp, 72.7% dry days) – urgent climate finance priority
- Ethiopia is coolest (16.1°C mean – highland advantage)
- Nigeria has highest flood risk (166mm max rain)
- Temperature differences are statistically significant (p < 0.001), justifying country-specific policies


3. Task 1: Environment Setup

- GitHub repo: climate-challenge-week0
- Branches: setup-task, eda-ethiopia, compare-countries, dashboard-dev
- Python venv with pandas, numpy, matplotlib, seaborn, streamlit
- GitHub Actions CI/CD workflow (linting + basic test)
- 3+ conventional commits merged via pull requests (e.g., feat: add data cleaning script, fix: handle missing DOY values)


4. Task 2: Data Cleaning & EDA

4.1 Cleaning Steps

1. Added Country column to each raw file
2. Converted YEAR + DOY to a single Date column
3. Replaced -999 (NASA POWER missing flag) with NaN
4. Forward-fill for missing values (max 3 consecutive days)
5. Retained outliers – climate extremes (e.g., heatwaves, extreme rain) are real and policy-relevant

4.2 Key Visualizations (with Findings)

[FIGURE 1: Monthly Temperature Trends (2015–2026) – Line Chart](src/plots/temperature_trends_all_countries.png)
Description: Five colored lines (one per country) showing average temperature by month over the full 11-year period. Sudan's line remains consistently highest across all months (peak at 32°C in May), while Ethiopia's line is lowest (peak at 18°C in March). All countries show a slight upward trend from 2015 to 2026 (~0.5-0.8°C increase).
Finding: Warming is consistent across all five nations, but Sudan's baseline heat makes it uniquely vulnerable to heatwaves.

[FIGURE 2: Monthly Precipitation Patterns – Bar Chart](src/plots/precipitation_trends_all_countries.png)
Description: Monthly average rainfall (mm/day) for each country. Nigeria shows a sharp peak in August–September (12 mm/day), while Sudan shows near-zero rainfall from November to March. Tanzania has a bimodal pattern (short rains in November, long rains in April–May).
Finding: Nigeria's extreme wet season poses flood risks; Sudan's extended dry season indicates drought pressure.

[FIGURE 3: Correlation Heatmap](src/plots/correlation_heatmaps_all_countries.png)
Description: Matrix showing correlation coefficients between temperature, precipitation, humidity, and dry days. Temperature and humidity show strong negative correlation (-0.78) in Sahelian countries (Sudan, Nigeria). Precipitation and dry days show near-perfect negative correlation (-0.94).
Finding: Hotter countries experience lower humidity (evaporative stress), exacerbating drought impacts.

[FIGURE 4: Precipitation Distribution (Log Scale) – Histogram](src/plots/precipitation_distribution_all_countries.png)
Description: Right-skewed distribution for all countries. Most days have <2mm rainfall, with a long tail extending to 166mm (Nigeria's maximum). Log transformation reveals that moderate rain days (2-10mm) are more common in Nigeria and Tanzania than in Sudan.
Finding: Extreme rainfall events are rare but severe – infrastructure must be designed for tail risks, not averages.

[FIGURE 5: Bubble Chart – Temperature vs Humidity (bubble size = rainfall)](src/plots/scatter_temp_humidity_all_countries.png)
Description: Scatter plot with temperature on x-axis, humidity on y-axis, and bubble size representing daily rainfall. Sudan clusters in high-temp, low-humidity region (large bubbles rare). Tanzania and Kenya cluster in moderate temp, moderate humidity with medium bubbles. Nigeria shows the largest bubbles (extreme rainfall) at moderate temperatures.
Finding: Extreme rainfall occurs at moderate temperatures (25-28°C), not at peak heat – flood risk is distinct from heat risk.

4.3 Cleaned Data Saved To

data/ethiopia_clean.csv, data/kenya_clean.csv, data/nigeria_clean.csv, data/sudan_clean.csv, data/tanzania_clean.csv


5. Task 3: Cross-Country Results

5.1 Temperature Summary

| Country | Mean Temp (°C) | Max Temp (°C) | Dry Days (% of year with <0.5mm rain) |
|---------|---------------|---------------|----------------------------------------|
| Ethiopia | 16.1 | 26.3 | 20.7% |
| Kenya | 20.4 | 31.0 | 6.3% |
| Nigeria | 26.7 | 36.2 | 11.8% |
| Sudan | 28.8 | 38.0 | 72.7% |
| Tanzania | 26.8 | 33.1 | 5.2% |

5.2 Precipitation Summary

| Country | Mean Rain (mm/day) | Max Rain (mm/day) | Flood Risk Indicator |
|---------|--------------------|-------------------|----------------------|
| Ethiopia | 3.6 | 82 | Moderate |
| Kenya | 1.5 | 52 | Low |
| Nigeria | 4.2 | 166 | High |
| Sudan | 0.6 | 67 | Low (but drought) |
| Tanzania | 3.7 | 123 | Moderate-High |

5.3 Statistical Test

- One-way ANOVA on mean daily temperatures across 5 countries
- F-statistic: 142.3
- p-value: < 0.001
- Conclusion: Differences between countries are statistically significant – not random variation. This justifies country-specific policy interventions rather than one-size-fits-all approaches.

5.4 Vulnerability Ranking (1 = most vulnerable)

| Rank | Country | Primary Hazard | Justification |
|------|---------|----------------|---------------|
| 1 | Sudan | Heat + Drought | 38°C max, 72.7% dry days |
| 2 | Nigeria | Flood | 166mm max rain |
| 3 | Ethiopia | Variable | Cool but erratic rains |
| 4 | Tanzania | Moderate | High max rain but balance |
| 5 | Kenya | Most balanced | Low dry days, moderate temp |


6. Bonus: Interactive Dashboard

Built with Streamlit. Features:
- Country multi-select (any combination of the 5 nations)
- Year slider (2015–2026)
- Variable selector (Temperature / Precipitation / Humidity)
- Two plot types: line chart (trend) + boxplot (distribution)
- Download filtered data as CSV (for COP32 delegates)

Screenshots: Stored in dashboard_screenshots/ folder in the repo.

Live Demo: [Streamlit App](https://climate-challenge-week0-cf86fc3wurgfhpdreq3zp7.streamlit.app/)


7. COP32 Policy Recommendations

| Priority | Action | Target Country/Region |
|----------|--------|----------------------|
| 1 | Climate finance for cooling & drought adaptation | Sudan (most urgent) |
| 2 | Heat early warning systems | All countries – Sudan first |
| 3 | Flood defense infrastructure | Nigeria (rainfall extremes) |
| 4 | Drought-resilient agriculture | Ethiopia, Sudan |
| 5 | Regional water infrastructure | Cross-border (Nile basin, Lake Victoria) |

7.1 Rationale for Priority 1 (Sudan)

- Highest mean (28.8°C) and max (38°C) temperatures
- 72.7% dry days → agricultural collapse risk
- Most statistically distinct from other nations (post-hoc Tukey HSD confirms)


8. Limitations & Future Work

8.1 Limitations of This Analysis

| Limitation | Explanation | Impact on Findings |
|------------|-------------|---------------------|
| Data source resolution | NASA POWER provides satellite estimates, not ground-truth station data | May smooth over microclimates; ground validation needed |
| Temporal coverage | 11 years (2015–2026) is sufficient for trends but not for long-term climate regime shifts | Cannot capture multi-decadal cycles (e.g., 30-year climate normals) |
| Missing data handling | Forward-fill assumes adjacent-day similarity; fails if sensor errors cluster | May underestimate variability in data-sparse regions |
| No socioeconomic data | Vulnerability ranking based solely on climate variables | Omits adaptive capacity, infrastructure, governance factors |
| Limited variables | Analyzed temperature, precipitation, humidity only | Excludes wind patterns, solar radiation, soil moisture |
| Single climate model | NASA POWER only – no ensemble comparison | Uncertainty bounds not quantified |

8.2 Future Work Recommendations

| Direction | Method | Policy Relevance |
|-----------|--------|------------------|
| Multi-model ensemble | Compare NASA POWER with ERA5, CHIRPS | Quantify uncertainty for high-stakes finance decisions |
| Downscaled projections | CMIP6 models at 5km resolution | 2030–2050 vulnerability forecasts |
| Socioeconomic integration | Combine with World Bank adaptive capacity indices | True vulnerability = climate hazard + exposure + adaptive capacity |
| Extreme event attribution | Statistical analysis of 1-in-100-year events | Infrastructure design standards |
| Cost-benefit modeling | Estimate adaptation ROI by country | Optimize COP32 finance allocation |
| Seasonal forecasting | Build predictive model for harvest planning | Early warning for food security |

8.3 Acknowledgment

This analysis does not replace national-level ground observations. COP32 delegates should use these findings as a strategic prioritization tool, not as the sole basis for funding decisions. Local validation is strongly recommended before implementation.


9. Conclusion

This analysis provides empirical, statistically robust evidence that:
1. Sudan faces the most extreme heat and drought – it must be a top recipient of COP32 adaptation finance.
2. Nigeria requires flood-focused infrastructure investment.
3. Ethiopia's highlands offer a cooler profile, but regional water cooperation remains essential.
4. The three-layer framework (reproducibility → cleaning → cross-country stats) ensured policy-grade outputs.

The interactive dashboard enables COP32 delegates to explore the data themselves, supporting transparent, evidence-based negotiations.

Limitations acknowledged: satellite data resolution, 11-year window, forward-fill assumptions, and absence of socioeconomic indicators. Future work will address these through multi-model ensembles, downscaled projections, and cost-benefit modeling.


10. Repository & Contact

GitHub Repository: https://github.com/nardos-tsige/climate-challenge-week0
Author: Nardos T.
Role: Climate Data Analyst, EthioClimate Analytics
