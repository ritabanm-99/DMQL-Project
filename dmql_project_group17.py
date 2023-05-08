# streamlit_app.py

import streamlit as st
import pandas as pd
import psycopg2

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

def get_data(query):
    with conn.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()
        # Convert the query results to a pandas DataFrame
        df = pd.DataFrame(data, columns=[desc[0] for desc in cur.description])
        return df
# Use Streamlit to display the retrieved data
st.header("Retail Database")
st.write("Enter a query to retrieve data from the database:")

query = st.text_input("Query:")
if query:
    df = get_data(query)
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No data found.")
# Retrieve all table names from the database
with conn.cursor() as cur:
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    table_names = [name[0] for name in cur.fetchall()]

# Display a dropdown menu with the table names
table_name = st.selectbox("Select the table Name:", table_names)

# If a table has been selected, display the data in a dataframe
if table_name:
    st.write(f"Displaying data from table: {table_name}")
    query = f"SELECT * FROM {table_name}"
    df = get_data(query)
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No data found.")
# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()

# rows = run_query("SELECT * from countries;")

# Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")


