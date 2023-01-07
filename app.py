import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5bf2370965189a4e182bdde9ae9a81be&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend(movie):
    movie_index=df[df['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommend_movies=[]
    recommend_movies_poster=[]
    for i in movies_list:
        movie_id=df.iloc[i[0]]['movie_id']
        # fetch postr of movie through api
        recommend_movies.append(df.iloc[i[0]]['title'])
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster

df=pickle.load(open('C:/Users/sande/OneDrive/Desktop/Python/movies.pkl','rb'))
similarity=pickle.load(open('C:/Users/sande/OneDrive/Desktop/Python/similarity_movie.pkl','rb'))
df=pd.DataFrame(df)

st.title('Movie Recommender System')
movie_name=st.selectbox('Write the Movie Name ',df['title'].values)

if st.button('Recommend'):
    name,poster=recommend(movie_name)
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])

    col4,col5,col6=st.columns(3)
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    with col6:
        st.text(name[5])
        st.image(poster[5])

    col7,col8,col9=st.columns(3)
    with col7:
        st.text(name[6])
        st.image(poster[6])
    with col8:
        st.text(name[7])
        st.image(poster[7])
    with col9:
        st.text(name[8])
        st.image(poster[8])


    st.text(name[9])
    st.image(poster[9],width=220)

