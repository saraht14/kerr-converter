
import streamlit as st
import pandas as pd

# Function to load the mapping file from the data folder
@st.cache_data
def load_mapping():
    return pd.read_csv("data/Final_Master_Product_Mapping.csv")

# Try to load the mapping file
try:
    mapping_df = load_mapping()
except FileNotFoundError:
    st.warning("Mapping file not found. Please upload the CSV file.")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        mapping_df = pd.read_csv(uploaded_file)
    else:
        st.stop()

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
