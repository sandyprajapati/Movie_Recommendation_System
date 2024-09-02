import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    
    # Make an API request
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=447fcf85538604c925dc3c275ec0ba78&language=en-US'.format(movie_id))
    
    # Check if the request was successful
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
    # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster

similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movies_dict.pkl','rb'))

movies=pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")



# Create the selectbox
selected_movie_name= st.selectbox('Choose a movie:', movies['title'].values)


if st.button('Recommend'):
    # Assuming recommend() returns movie names and posters
    names, posters = recommend(selected_movie_name)
    
    # Create columns for the recommendations (e.g., 3 movie recommendations)
    col1, col2, col3,col4,col5 = st.columns(5)

    # Populate the columns with movie recommendations
    with col1:
        st.text(names[0])  # Movie name 1
        st.image(posters[0])  # Movie poster 1

    with col2:
        st.text(names[1])  # Movie name 2
        st.image(posters[1])  # Movie poster 2

    with col3:
        st.text(names[2])  # Movie name 3
        st.image(posters[2])  #
    with col4:
        st.text(names[3])  # Movie name 4
        st.image(posters[3])  #
    with col5:
        st.text(names[4])  # Movie name 5
        st.image(posters[4])  #







        