from fastapi import FastAPI
from consultas import *
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Permite cualquier origen(dominio)
    allow_credentials=False, # Debe ser False si usas "*" em origins
    allow_methods=["*"],     # Permite todos los métodos HTTP (GET,POST,PUT,DELETE, etc)
    allow_headers=["*"],     # Permite todas las cabeceras HTTP
)

class ModelCommentPost(BaseModel):
    id_pelicula: str
    persona: str
    comentario: str
    fecha: str

class ModelRatingPost(BaseModel):
    id_pelicula: str
    persona: str
    calificacion: int
    fecha: str

@app.get('/movies/{name}', tags=['Peliculas'])
def get_list_movies(name: str, year: str = None):
    final_url = get_movie_list_url(name, year)
    return get_url_result(final_url)

@app.get('/movie/title/{name}', tags=['Peliculas'])
def get_movie_title(name: str, year: str = None):
    final_url = get_movie_url(SearchType.TITLE, name)
    return get_url_result(final_url)

@app.get('/movie/{id}', tags=['Peliculas'])
def get_movie_id(id: str):
    if id.startswith("tt") and id[2:].isdigit():
        print("ID válido")
    else:
        print("ID inválido")
    final_url = get_movie_url(SearchType.ID, id)
    result = get_url_result(final_url)
    all_comments = get_movie_comments(id)
    avg_rating = average_rating(get_movie_rating(id))
    result['comments'] = all_comments
    result['avgRating'] = avg_rating
    return result

@app.post('/comment', tags=['Comentarios'])
def create_comment(comment: ModelCommentPost):
    try:
        insert_comment([comment.id_pelicula, comment.persona, comment.comentario, comment.fecha])
        return {'mensaje': 'registro correcto del comentario'}
    except sqlite3.Error as error:
        print(error)
        return {'error': 'ha fallado el registro del comentario'}

@app.post('/rating', tags=['Calificaciones'])
def create_rating(rating: ModelRatingPost):
    try:
        insert_rating([rating.id_pelicula, rating.persona, rating.calificacion, rating.fecha])
        return {'mensaje': 'registro correcto de la calificación'}
    except sqlite3.Error as error:
        print(error)
        return {'error': 'ha fallado el registro de la calificación'}