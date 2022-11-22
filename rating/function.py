import sqlite3


def get_films_by_rating_children():
    """
    :return: Возвращает список словарей фильмов с rating G
    """
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G'
        """
        cur.execute(sqlite_query)
        data = cur.fetchall()

        films_list = []

        for i in data:
            film = {
                'title': i[0],
                'rating': i[1],
                'description': i[2]
            }
            films_list.append(film)

    return films_list


def get_films_by_rating_family():
    """
    :return: Возвращает список словарей фильмов с rating G, PG, PG-13
    """
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
        """
        cur.execute(sqlite_query)
        data = cur.fetchall()

        films_list = []

        for i in data:
            film = {
                'title': i[0],
                'rating': i[1],
                'description': i[2]
            }
            films_list.append(film)

    return films_list


def get_films_by_rating_adult():
    """
    :return: Возвращает список словарей фильмов с rating R, NC-17
    """
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'R' OR rating = 'NC-17'
        """
        cur.execute(sqlite_query)
        data = cur.fetchall()

        films_list = []

        for i in data:
            film = {
                'title': i[0],
                'rating': i[1],
                'description': i[2]
            }
            films_list.append(film)

    return films_list
