import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Dashboard 📺")
st.sidebar.markdown("# Home Page")

df = pd.read_csv(r'data/ratings.csv')
st.write(df)