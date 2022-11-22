import sqlite3
from pprint import pprint


def get_actors_in_together(actor_1, actor_2):
    """
    :param actor_1: Принимает имя в любом регистре первого актера,
    :param actor_2: Принимает имя в любом регистре второго актера,
    :return: возвращает список актеров, которые играли в фильме с этой парой более 2-х раз
    """
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT netflix.cast
                    FROM netflix
                    WHERE netflix.cast LIKE '%{actor_1}%'
                    AND netflix.cast LIKE '%{actor_2}%'
                    
        """
        cur.execute(sqlite_query)
        # data равна списку словарей актеров (cast) которые имею в списке переданных в качестве аргумента двух актеров
        data = cur.fetchall()
        # list_cast_more_two это список, который получает всех актеров кроме переданных в аргументе, равные
        # тому количеству раз, сколько они в сумме встречались во всех картежах в data
        list_cast_more_two = []
        # list_actors это список, который получает всех актеров из списка list_cast_more_two которые встречаются там
        # 2 и более раз
        list_actors = []

        for actors_tuple in data:  # Пробегаюсь по кортежам списка
            for casts_str in actors_tuple:  # Пробегаюсь по строке итерируемого кортежа
                actors_list = casts_str.split(', ')  # создаю переменную равной списку полученный разделением
                # итерируемой строки на отдельные имена
                for actor in actors_list:  # Пробегаюсь по каждому актеру итерируемого кортежа
                    if actor_1 != actor and actor_2 != actor:  # Добавляю в список всех актеров за исключением
                        # переданных
                        list_actors.append(actor)

        for actor in list_actors:  # Пробегаюсь по списку из повторяющихся актеров и добавляю в новый список только тех
            #  кто встречается там 2 или более раз
            if list_actors.count(actor) >= 2:
                list_cast_more_two.append(actor)
        # Так как актеры которые играли вместе с переданными в аргументы актероами в списке list_cast_more_two
        # дублируются, превращаю их в множество, тем самым исключая повторения и
        # получившийся результат возвращаю в список
        return list(set(list_cast_more_two))


def find_a_movie(film_type, release_year, genre):
    with sqlite3.connect('netflix.db') as con:
        cur = con.cursor()
        sqlite_query = f"""
                    SELECT type, release_year, title, description
                    FROM netflix
                    WHERE type = '{film_type}'
                    AND release_year = '{release_year}'
                    AND listed_in LIKE '%{genre}%'
                    LIMIT 10
        """

        cur.execute(sqlite_query)
        data = cur.fetchall()

    return data


#  Для проверки функции get_actors_in_together
# pprint(get_actors_in_together('Rose McIver', 'Ben Lamb'))

#  Для проверки функции find_a_movie
# pprint(find_a_movie('Movie', 2016, 'Dramas'))