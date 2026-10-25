import requests
from conexion import Conexion
import sqlite3
from urllib.parse import quote_plus
from enum import Enum

URL = 'https://www.omdbapi.com'
APIKEY = '1edead43'

class SearchType(Enum):
    ID = 1
    TITLE = 2

def formato(response):
    result_list = []

    for fila in response.fetchall():
        dic = dict(fila)
        result_list.append(dic)

    return result_list

def valid_year(year):
    result = True
    if len(year) != 4:
        result = False

    if not (int(year) >= 1876 and int(year) <= 2026):
        result = False

    return result

def get_movie_url(search_type, reference, year = None):
    """
    Recibe el tipo de busqueda, puede ser el imdb ID o el titulo de la pelicula.
    Se une la URL base con la APIKEY y dependiendo del tipo de busqueda se agrega 
    la referencia correspondiente 
    """
    movie_url = f'{URL}/?apikey={APIKEY}'
    if search_type == SearchType.ID:
        movie_url = f'{movie_url}&i={reference}'
    elif search_type == SearchType.TITLE:
        new_reference = quote_plus(reference)
        movie_url = f'{movie_url}&t={new_reference}'
        if year is not None and valid_year(year):
            movie_url = f'{movie_url}&y={year}'
    else:
        raise Exception('El tipo de busqueda para la pelicula es incorrecto')

    return movie_url

def get_movie_list_url(reference, year = None):
    """
    Formamos la URL que sera usada para obtener el listado de películas
    """
    
    movie_url = f'{URL}/?apikey={APIKEY}'
    if reference is None:
        raise Exception('No se ingreso el nombre de la pelicula')

    new_reference = quote_plus(reference)
    movie_url = f'{movie_url}&s={new_reference}'

    if year is not None:
        movie_url = f'{movie_url}&y={new_reference}'

    return movie_url

def get_url_result(url):
    """
    Recibe la url para hacer la busqueda de la información 
    devuelve un JSON 
    """
    try:
        result = requests.get(url)
        movie_information = result.json()
        return movie_information
    except:
        raise Exception('Error: no se pudo obtener la información')

def get_movie_comments(imdbID: str):
    try:
        connectionGetComments = Conexion(f'SELECT * FROM Comentario WHERE id_pelicula = ?;', (imdbID,))
        filas = connectionGetComments.res
        result_list = formato(filas)
        connectionGetComments.close()
        return result_list
    except sqlite3.Error as error:
        raise Exception('Error: ', error)

def insert_comment(data: list):
    try:
        connectionInsertComment = Conexion(f'INSERT INTO Comentario(id_pelicula, persona, comentario, fecha) VALUES(?, ?, ?, ?);', data)
        connectionInsertComment.connection.commit()
    except sqlite3.Error as error:
        raise Exception('Error: ', error)
    connectionInsertComment.close()

def get_movie_rating(imdbID: str):
    try:
        connectionGetRatings = Conexion(f'SELECT * FROM Calificacion WHERE id_pelicula = ?;', (imdbID,))
        filas = connectionGetRatings.res
        result_list = formato(filas)
        connectionGetRatings.close()
        return result_list
    except sqlite3.Error as error:
        raise Exception('Error: ', error)

def average_rating(ratings):
    result = 0
    sum = 0

    for rating in ratings:
        sum += rating['calificacion']

    if len(ratings) != 0:
        result = sum/len(ratings)

    return result

def insert_rating(data: list):
    try:
        connectionInsertRating = Conexion(f'INSERT INTO Calificacion(id_pelicula, persona, calificacion, fecha) VALUES(?, ?, ?, ?);', data)
        connectionInsertRating.connection.commit()
    except sqlite3.Error as error:
        raise Exception('Error: ', error)
    connectionInsertRating.close()
