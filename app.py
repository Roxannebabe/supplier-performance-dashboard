import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Supplier Performance Dashboard", layout="wide")
st.title("Supplier Performance & Procurement Decision Dashboard")
st.markdown("**Target User:** E-commerce Procurement Manager")

df = pd.read_csv('supplier_summary.csv')

st.sidebar.header("Filters")
selected_vendors = st.sidebar.multiselect("Select Suppliers", df['VendorName'].unique(), default=df['VendorName'].head(10).tolist())
min_spend = st.sidebar.slider("Minimum Total Spend ($)", min_value=int(df['Total_Spend'].min()), max_value=int(df['Total_Spend'].max()), value=int(df['Total_Spend'].min()))

filtered_df = df[(df['VendorName'].isin(selected_vendors)) & (df['Total_Spend'] >= min_spend)]

st.subheader("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Suppliers", len(filtered_df))
col2.metric("Total Spend", f"${filtered_df['Total_Spend'].sum():,.0f}")
col3.metric("Avg On-Time Rate", f"{filtered_df['OnTime_Rate'].mean():.1f}%")
col4.metric("Avg Lead Time", f"{filtered_df['Avg_LeadTime'].mean():.1f} days")

st.subheader("Top Suppliers by Total Spend")
top10 = filtered_df.head(10)
fig1 = px.bar(top10, x='VendorName', y='Total_Spend', title='Top 10 Suppliers by Total Spend', color='Total_Spend')
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Lead Time vs On-Time Rate")
fig2 = px.scatter(filtered_df, x='Avg_LeadTime', y='OnTime_Rate', size='Total_Spend', hover_name='VendorName', title='Supplier Risk Analysis', labels={'Avg_LeadTime': 'Average Lead Time (days)', 'OnTime_Rate': 'On-Time Rate (%)'})
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Detailed Supplier Table")
st.dataframe(filtered_df.sort_values('Total_Spend', ascending=False), use_container_width=True)

st.download_button("Download Full Supplier Report", filtered_df.to_csv(index=False).encode('utf-8'), "supplier_report.csv", "text/csv")