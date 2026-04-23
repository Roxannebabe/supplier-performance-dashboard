# supplier-performance-dashboard
Interactive Supplier Performance Dashboard for E-commerce Procurement

# Supplier Performance & Procurement Decision Dashboard

## Project Overview
This is an interactive Streamlit dashboard for e-commerce / retail procurement managers.  
It helps users quickly evaluate suppliers, compare performance (spend, lead time, on-time rate), and make better purchasing decisions.

## Target User
E-commerce Procurement Manager who needs to select reliable suppliers and control costs.

## Dataset
- Source: Vendor Performance Analysis Dataset (Kaggle)  https://www.kaggle.com/datasets/harshmadhavan/vendor-performance-analysis?resource=download&select=purchases.csv
- Accessed: April 2026  
- Because the original dataset is too large, I used a simple random sample (purchases_sample_25mb.csv) for GitHub upload

## Key Features
- Interactive filters (supplier selection + minimum spend)
- Real-time KPI cards
- Top suppliers bar chart
- Lead time vs On-time rate scatter plot
- Full sortable data table
- One-click CSV download

## How to Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

## Files in this repo
- app.py → Streamlit dashboard
- supplier_dashboard.ipynb → Full Python analysis workflow
- purchases_sample_25mb.csv → Sample data
- supplier_summary.csv → Pre-calculated supplier KPIs
- requirements.txt → Dependencies

## Technologies
Python, pandas, Plotly, Streamlit

## Author
Yuqi Li
