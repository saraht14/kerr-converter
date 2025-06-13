
import streamlit as st
import pandas as pd

# Load the mapping file
@st.cache_data
def load_mapping():
    return pd.read_csv("data/Final_Master_Product_Mapping.csv")

mapping_df = load_mapping()

# Streamlit app interface
st.title("Product Number Lookup")

product_number = st.text_input("Enter Manufacturer Product Number")

if product_number:
    result = mapping_df[mapping_df["Manufacturer_Product_Number"].str.upper() == product_number.upper()]
    if not result.empty:
        st.success("Match found!")
        st.dataframe(result)
    else:
        st.warning("No match found.")
