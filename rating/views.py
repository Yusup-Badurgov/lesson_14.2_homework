from flask import jsonify, Blueprint
from rating.function import get_films_by_rating_children, get_films_by_rating_family, get_films_by_rating_adult

rating_blp = Blueprint('rating_blp', __name__, url_prefix='/rating/')


@rating_blp.route('/children/')
def view_rating_children():
    films = get_films_by_rating_children()
    return jsonify(films)


@rating_blp.route('/family/')
def view_rating_family():
    films = get_films_by_rating_family()
    return jsonify(films)


@rating_blp.route('/adult/')
def view_rating_adult():
    films = get_films_by_rating_adult()
    return jsonify(films)