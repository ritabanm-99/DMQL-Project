import streamlit as st
import pandas as pd
import numpy as np
import tempfile
import sqlite3

st.title("Warehouse Data")
#st.image('./img.jpg')
st.markdown("""In this interactive streamlit dashboard, we have attempted to implement 
an interactive interface for warehouse and retail managers to get quick insights on E-commerce Data.""")
st.subheader("Tap here to view the data:")

#Create a variable for each table. 
Cancelled_orders = pd.read_csv("./CancelledOrders.csv")
Orders = pd.read_csv("./Orders.csv")
Suppliers = pd.read_csv("./Suppliers.csv") 
Customers = pd.read_csv("./Customers.csv")

Catalog = pd.read_csv("./Catalog.csv") 
Products = pd.read_csv("./Products.csv")

#To-do: Do we want a sidebar? what other features do we want to add?
#with st.sidebar:
option = st.selectbox('Which Table would you like to see?', ('Cancelled Orders', 'Orders','Customers', 'Catalog', 'Products','Suppliers'))
if option == 'Cancelled Orders':
    st.title("Cancelled Orders")
    st.write(Cancelled_orders)

if option == 'Online_Retail':
    st.title("Online Retail!")
    st.write(Online_Retail)  

if option == 'Orders':
    st.title("Orders")
    st.write(Orders)

if option == 'Customers':
    st.title("Customers!")
    st.write(Customers)

if option == 'Products':
    st.title("Products!")
    st.write(Products)

if option == 'Catalog':
    st.title("Catalog!")
    st.write(Catalog)

if option == 'Suppliers':
    st.title("Suppliers")
    st.write(Suppliers)
