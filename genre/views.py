from flask import Blueprint, jsonify
from genre.function import get_films_by_genre

genre_blp = Blueprint('genre_blp', __name__)


@genre_blp.route('/genre/<genre>/')
def view_by_genre(genre):
    films = get_films_by_genre(genre)
    return jsonify(films)
