# dashboard/app.py

import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Import SQL queries
from sql_queries import (
    get_top_states_query,
    get_yearwise_trend_query,
    get_transaction_types_query,
    get_quarterly_growth_query
)

# Set up the page
st.set_page_config(page_title="📊 PhonePe Dashboard", layout="wide")
st.title("📱 PhonePe Pulse Transaction Insights")

# Connect to SQLite
conn = sqlite3.connect("phonepe.db")

# Sidebar
st.sidebar.header("📌 Select View")
query_type = st.sidebar.radio("Choose Insight", [
    "Top States by Transaction Amount",
    "Year-wise Trends",
    "Top Transaction Types",
    "Quarterly Growth"
])

# Routing based on user selection
if query_type == "Top States by Transaction Amount":
    df = pd.read_sql_query(get_top_states_query(), conn)
    fig = px.bar(df, x='total_amount', y='state', orientation='h',
                 title="Top 10 States by Transaction Amount", color='total_amount',
                 color_continuous_scale="Viridis")
    st.plotly_chart(fig, use_container_width=True)

elif query_type == "Year-wise Trends":
    df = pd.read_sql_query(get_yearwise_trend_query(), conn)
    fig = px.line(df, x='year', y='total_amount', markers=True,
                  title="Year-wise Transaction Trend", color_discrete_sequence=["blue"])
    st.plotly_chart(fig, use_container_width=True)

elif query_type == "Top Transaction Types":
    df = pd.read_sql_query(get_transaction_types_query(), conn)
    fig = px.pie(df, names='transaction_type', values='total_amount',
                 title="Transaction Type Distribution")
    st.plotly_chart(fig, use_container_width=True)

elif query_type == "Quarterly Growth":
    df = pd.read_sql_query(get_quarterly_growth_query(), conn)
    df['period'] = df['year'].astype(str) + ' Q' + df['quarter'].astype(str)
    fig = px.bar(df, x='period', y='total_amount',
                 title="Quarterly Transaction Growth", color='total_amount',
                 color_continuous_scale="blues")
    st.plotly_chart(fig, use_container_width=True)

conn.close()
