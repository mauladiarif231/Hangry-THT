
import streamlit as st
import pandas as pd

# Load data
daily_sales = pd.read_csv(r'D:\Mnet-Maul\Data Engineering\Maul\Proses Test Masuk Kerja\Hangry\mage.ai\your_first_project\data_exporters\Destination\daily_sales.csv')
weekly_sales = pd.read_csv(r'D:\Mnet-Maul\Data Engineering\Maul\Proses Test Masuk Kerja\Hangry\mage.ai\your_first_project\data_exporters\Destination\weekly_sales.csv')
ytd_sales = pd.read_csv(r'D:\Mnet-Maul\Data Engineering\Maul\Proses Test Masuk Kerja\Hangry\mage.ai\your_first_project\data_exporters\Destination\ytd_sales.csv')

# Convert date columns to datetime
daily_sales['date'] = pd.to_datetime(daily_sales['week'])

# Create dashboard
st.title('Sales Dashboard')

# Daily Sales Trends
st.subheader('Daily Sales Trends')
st.line_chart(daily_sales.set_index('date')[['gross_revenue', 'cogs', 'discount', 'net_profit']])

# Weekly Sales Trends
st.subheader('Weekly Sales Trends')
st.bar_chart(weekly_sales.set_index('week')[['gross_revenue', 'cogs', 'discount', 'net_profit']])

# Year-To-Date Sales
st.subheader('Year-To-Date Sales')
st.area_chart(ytd_sales.set_index('year')[['gross_revenue', 'cogs', 'discount', 'net_profit']])
