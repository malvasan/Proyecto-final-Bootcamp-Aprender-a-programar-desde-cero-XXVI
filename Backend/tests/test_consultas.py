import pytest
from consultas import *

def test_url_movie_id():

    assert get_movie_url(SearchType.ID, 'tt4589218') == 'https://www.omdbapi.com/?apikey=1edead43&i=tt4589218'


def test_url_movie_title():

    assert get_movie_url(SearchType.TITLE, "Five Nights at Freddy's") == 'https://www.omdbapi.com/?apikey=1edead43&t=Five+Nights+at+Freddy%27s'

def test_url_movie_title():

    assert get_movie_url(SearchType.TITLE, "Five Nights at Freddy's", '2023') == 'https://www.omdbapi.com/?apikey=1edead43&t=Five+Nights+at+Freddy%27s&y=2023'


def test_url_list_movies():

    assert get_movie_list_url("Five Nights at Freddy's") == 'https://www.omdbapi.com/?apikey=1edead43&s=Five+Nights+at+Freddy%27s'