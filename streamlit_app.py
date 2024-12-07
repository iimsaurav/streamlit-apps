import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px

# Snowflake Connection Configuration
snowflake_connection = {
    "user": "kgaurav765",
    "password": "Global@12345   ",
    "account": "aedkavs-is37277",
    "warehouse": "COMPUTE_WH",
    "database": "SNOWFLAKE_SAMPLE_DATA",
    "schema": "TPCH_SF1"
}

# Create a function to connect to Snowflake
def create_connection():
    conn = snowflake.connector.connect(
        user=snowflake_connection["user"],
        password=snowflake_connection["password"],
        account=snowflake_connection["account"],
        warehouse=snowflake_connection["warehouse"],
        database=snowflake_connection["database"],
        schema=snowflake_connection["schema"]
    )
    return conn

# Query to fetch data from the Order table
def fetch_data(customer_key=None):
    query = f"""
        SELECT
            O_ORDERKEY,
            O_ORDERDATE,
            O_CUSTKEY,
            O_TOTALPRICE,
            O_ORDERPRIORITY,
            O_ORDERSTATUS
        FROM orders
    """
    if customer_key:
        query += f" WHERE O_CUSTKEY = {customer_key}"
    
    conn = create_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    
    # Ensure O_ORDERDATE is a datetime column
    df['O_ORDERDATE'] = pd.to_datetime(df['O_ORDERDATE'])
    
    return df

# Streamlit UI setup
st.title('Snowflake Orders Dashboard')

# Filter: Customer Key
customer_key = st.selectbox("Select Customer Key", [None] + list(range(1, 100)))  # Adjust based on your customer keys

# Fetch Data
data = fetch_data(customer_key)

# Display data preview
st.write(f"Showing data for Customer Key: {customer_key}" if customer_key else "Showing all data")
st.write(data.head())

# Visualization 1: Total Price Over Time
fig1 = px.line(data, x='O_ORDERDATE', y='O_TOTALPRICE', title="Total Price Over Time")
st.plotly_chart(fig1)

# Visualization 2: Order Count by Order Priority
fig2 = px.bar(data, x='O_ORDERPRIORITY', title="Order Count by Order Priority")
st.plotly_chart(fig2)
