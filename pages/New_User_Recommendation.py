import streamlit as st
import pandas as pd

st.markdown("## New User Movie Recommendation")
st.sidebar.markdown("# New User")

def load_data():
    global ratings_df
    ratings_df = pd.read_csv("./data/ratings.csv")
    global movies_df
    movies_df = pd.read_csv('./data/movies.csv')
    global ratings_grp_by_movie
    ratings_grp_by_movie = ratings_df.groupby('movieId')['rating'].mean()
    global movies_ratings_df
    movies_ratings_df = movies_df.merge(ratings_grp_by_movie, left_on='movieId', right_on='movieId')

def getTopRatedMovies():
    return movies_ratings_df

if __name__=="__main__":
    load_data()

option = st.selectbox(
    'How would like movies to be recommended',
    ('Top Rated', 'Similar Movies', 'Top Rated By Genre')
)
recommendations = None
if option == 'Top Rated':
    recommendations = movies_ratings_df.sort_values(by=['rating'], ascending=False)
elif option == 'Similar Movies':
    st.write('Similar Movie Recommendation')
elif option == 'Top Rated By Genre':
    st.write("Top Rated Movies By Genre")

st.markdown("### Recommendations")
st.write(recommendations)