import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Dashboard 📺")
st.sidebar.markdown("# Home Page")

rating_df = pd.read_csv(r'data/ratings.csv')
grp_by_rating = rating_df.groupby('rating')['movieId'].count()
st.subheader('Rating Distribution')
st.bar_chart(grp_by_rating)

st.subheader('Most Watched Movies')
st.subheader('Top Rated ')