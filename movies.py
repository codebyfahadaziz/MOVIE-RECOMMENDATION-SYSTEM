'''import streamlit as st
import pickle
import pandas as pd

# Load the pickle files
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Convert to DataFrame
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')


# Function to get recommended movies
def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['title'])
    return recommended_movies


# Selectbox to choose movie title
selected_movie_name = st.selectbox(
    'Choose a movie',
    movies['title'].values
)

# Recommend button
if st.button('Recommend'):
    recommendations = recommended(selected_movie_name)
    st.write("Recommended movies:")
    for movie in recommendations:
        st.write(movie)'''
import streamlit as st
import pickle
import pandas as pd
import requests

# TMDb Bearer Token (v4 API key)
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YmU0OTY0MjA4NDM0OTUzMDU2MGZmNDQ3YTVlNDJlYiIsIm5iZiI6MTc1NDY2ODcyMy41NzIsInN1YiI6IjY4OTYxZWIzNmJlNDYzOWQ5YWM0YjJiNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Xy41JuOnyuU4wteMH8VywIVns-9n71DWi8tKlXiZ9pk"

# Load the pickle files
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Convert to DataFrame
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommendation System')

# Function to fetch poster from TMDb
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

# Function to get recommended movies and posters
def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Selectbox to choose movie title
selected_movie_name = st.selectbox(
    'Choose a movie',
    movies['title'].values
)

# Recommend button
if st.button('Recommend'):
    names, posters = recommended(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.caption(names[i])

