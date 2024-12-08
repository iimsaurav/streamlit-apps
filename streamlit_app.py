# Import python packages
from snowflake.snowpark.context import get_active_session

# Write directly to the ap

# Get the current credentials
session = get_active_session()

import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px

# Snowflake Connection Configuration

# Query to fetch data from the Order table


# Streamlit UI setup
st.title('Snowflake Orders Dashboard')

# Filter: Customer Key
customer_key = st.selectbox("Select Customer Key", [None] + list(range(1, 100)))  # Adjust based on your customer keys

# Fetch Data
data = session.table("product")


# Visualization 1: Total Price Over Time
fig1 = px.line(data, x='O_ORDERDATE', y='O_TOTALPRICE', title="Total Price Over Time")
st.plotly_chart(fig1)

# Visualization 2: Order Count by Order Priority
fig2 = px.bar(data, x='O_ORDERPRIORITY', title="Order Count by Order Priority")
st.plotly_chart(fig2)

