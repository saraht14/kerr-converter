import streamlit as st
import pandas as pd

# Load the product mapping CSV file
product_mapping = pd.read_csv('product_mapping.csv')

# Streamlit app
st.title('Product Number Conversion App')

# Input field for Manufacturer Product Number
manufacturer_number = st.text_input("Enter Manufacturer Product Number:")

if manufacturer_number:
    # Look up the Manufacturer Product Number in the product mapping
    result = product_mapping[product_mapping['Manufacturer_Product_Number'] == manufacturer_number]
    
    if not result.empty:
        # Display the corresponding Kerr Product Number and Manufacturer
        kerr_number = result['Kerr_Product_Number'].values[0]
        manufacturer = result['Manufacturer'].values[0]
        st.success(f"Kerr Product Number: {kerr_number}")
        st.success(f"Manufacturer: {manufacturer}")
    else:
        st.error("Manufacturer Product Number not found.")
