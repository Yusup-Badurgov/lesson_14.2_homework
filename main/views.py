from flask import jsonify, Blueprint, redirect

from main.function import get_film_by_title, get_films_by_years

main_blp = Blueprint('main_blp', __name__, url_prefix='/movie/')
main_blp_exception_prefix = Blueprint('main_blp_exception_prefix', __name__)


@main_blp_exception_prefix.route('/')
def index_page():
    return redirect("/movie/Zubaan/", code=302)
# Тут значение указано по умолчанию. Иногда забываешь, что у тебя нет главной вьюшки "/" и после запуска сервера
# естественно выходит ошибка. Потом ищешь ее по всему коду, хотя ты просто забыл дописать URL. Это вьюшка во
# избежания этого. Делает переадресацию по первой вьюшке, так как главной не существует.


@main_blp.route('/<title>/')
def view_by_title(title):
    film = get_film_by_title(title)
    return jsonify(film)


@main_blp.route('/<year_1>/to/<year_2>/')
def view_by_years(year_1, year_2):
    films = get_films_by_years(year_1, year_2)
    return jsonify(films)
