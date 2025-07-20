import streamlit as st
import pickle
import pandas as pd

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)

    return recommended_movies

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title(" Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie you like:", movies["title"].values)

if st.button("Recommend"):
    names = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")
    for name in names:
        st.write(f" {name}")
