import sqlite3


def get_film_by_title(title):
    """
    :param title: Принимает название фильма,
    :return: Возвращает словарь по названию фильма
    """
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title LIKE '%{title}%' 
        """
        cur.execute(sqlite_query)
        data = cur.fetchone()

        film_dict = {
            'title': data[0],
            'country': data[1],
            'release_year': data[2],
            'genre': data[3],
            'description': data[4]
        }

    return film_dict


def get_films_by_years(year_1, year_2):
    """
    :param year_1: принимает ОТ какого года фильмы нужны,
    :param year_2: принимает ДО какого года фильмы нужны,
    :return: возвращает список словарей(фильмов)
    """
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {year_1} AND {year_2}
                    LIMIT 100
        """
        cur.execute(sqlite_query)
        data = cur.fetchall()

        films_list = []

        for i in data:
            film = {
                'title': i[0],
                'release_year': i[1]
            }

            films_list.append(film)

        return films_list
