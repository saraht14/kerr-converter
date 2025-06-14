
import streamlit as st
import pandas as pd

# Load the product mapping CSV (single .csv)
product_mapping = pd.read_csv('product_mapping.csv')

# Streamlit app layout
st.title("Kerr Product Number Finder")

# Text input for Manufacturer Product Number
user_input = st.text_input("Enter Manufacturer Product Number:")

# Search and display result
if user_input:
    result = product_mapping[product_mapping['Manufacturer_Product_Number'].str.strip().str.upper() == user_input.strip().str.upper()]
    
    if not result.empty:
        st.success(f"Kerr Product Number: {result.iloc[0]['Kerr_Product_Number']}")
        st.write(f"Manufacturer: {result.iloc[0]['Manufacturer']}")
    else:
        st.error("No matching product found.")
