def recommend(movie): 
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity.loc[movie_index]
    print(type(distances))
    print(distances)