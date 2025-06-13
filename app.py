import streamlit as st
import pandas as pd

# Load the product mapping CSV file
df = pd.read_csv('product_mapping.csv')

# Display the dataframe in the Streamlit app
st.title('Product Mapping')
st.write(df)
