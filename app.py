import streamlit as st
import pandas as pd

# 1. Configure the web page
st.set_page_config(page_title="Auto Insurance Matrix", layout="centered")
st.title("Auto Insurance Terminology Comparison")

# 2. Load the data (Streamlit caches this so it's fast)
@st.cache_data
def load_data():
    return pd.read_csv("matrix_data.csv")

df = load_data()

# 3. Set up the dropdown options
states = df['State'].unique().tolist()
carriers = df.columns[2:].tolist() 

# 4. Create the interactive widgets side-by-side
col1, col2, col3 = st.columns(3)
with col1:
    selected_state = st.selectbox('Select State:', states)
with col2:
    c1 = st.selectbox('Carrier 1:', carriers, index=0)
with col3:
    c2 = st.selectbox('Carrier 2:', carriers, index=1)

# 5. Filter the data
filtered_df = df[df['State'] == selected_state][[c1, c2]]

# 6. Display the table
st.markdown("---")
st.subheader(f"{c1} vs. {c2} in {selected_state}")
st.dataframe(filtered_df, hide_index=True, use_container_width=True)
