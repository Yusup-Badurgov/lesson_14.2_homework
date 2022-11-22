import sqlite3


def get_films_by_genre(genre):
    """
    :param genre: Принимает жанр фильмов
    :return: возвращает список словарей фильмов по указанному жанру
    """
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE listed_in LIKE "%{genre}%"
                    ORDER BY release_year DESC
                    LIMIT 10
        """
        cur.execute(sqlite_query)
        data = cur.fetchall()
        films_list = []

        for i in data:
            films = {
                'title': i[0],
                'description': i[1]
            }
            films_list.append(films)

    return films_list
