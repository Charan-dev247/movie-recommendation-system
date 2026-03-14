import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

df = pd.merge(ratings, movies, on="movieId")

movie_matrix = df.pivot_table(
    index='userId',
    columns='title',
    values='rating'
)

movie_matrix_filled = movie_matrix.fillna(0)

similarity = cosine_similarity(movie_matrix_filled.T)

similarity_df = pd.DataFrame(
    similarity,
    index=movie_matrix.columns,
    columns=movie_matrix.columns
)

def recommend_movies(movie_name, n=5):
    similar_movies = similarity_df[movie_name].sort_values(ascending=False)
    return similar_movies.iloc[1:n+1]

st.title("Movie Recommendation System")

movie = st.selectbox(
    "Select a movie",
    movie_matrix.columns
)

if st.button("Recommend"):
    recommendations = recommend_movies(movie)
    st.write("Recommended Movies:")
    for m in recommendations.index:
        st.write(m)