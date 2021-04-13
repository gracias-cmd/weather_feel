# все для баз данных
import sqlite3
from sqlite3 import Error


DATABASE = 'database.db'
connection = None

#utils for database
def get_cursor():
    global connection
    if connection is None:
        connection = sqlite3.connect(DATABASE, check_same_thread=False)
        print("New connection created")
    else:
        print("Connection already exists")
    return connection.cursor()


def commit():
    global connection
    connection.commit()


def close_connection():
    global connection
    connection.close()
    print("Connection closed")


# создание базы если нет или подключение базы sqlite и создание таблицы
def init_database():
    # создание базы если нет или подключение базы

    # подключение курсора
    cursor = get_cursor()
    # создание таблицы если ее не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_settings (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            first_name  TEXT,
            last_name   TEXT,
            city        TEXT,
            lang        TEXT,
            notify      TEXT,
            signup_date TEXT
        )
    ''')
    # сохранить изменения
    commit()

    # подключение курсора
    cursor = get_cursor()
    # создание таблицы если ее не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_meteo_data (
            id              INTEGER PRIMARY KEY,
            user_id         INTEGER NOT NULL,
            wellness_score  INTEGER,
            backpain_data   INTEGER,
            headpain_data   INTEGER,
            time_data       TEXT,
            current_city    TEXT,
            temperature     REAL,
            real_feel       REAL,
            air_pressure    INTEGER,
            humidity        REAL
        )
    ''')
    # сохранить изменения
    commit()


## База
# сохранять ID пользователя если ID нет базе
def write_id_to_database(user_id: int, first_name: str, last_name: str):
    cursor = get_cursor()
    cursor.execute('INSERT INTO user_settings (user_id, first_name, last_name) VALUES (?, ?, ?)', (user_id, first_name, last_name))
    commit()

def set_user_language(user_id: int, lang: str):
    cursor = get_cursor()
    cursor.execute('INSERT INTO user_settings (lang) VALUES (?) WHERE user_id=?', (lang, user_id,))
    commit()

def set_user_city(user_id: int, city: str):
    cursor = get_cursor()
    cursor.execute('INSERT INTO user_settings (city) VALUES (?) WHERE user_id=?', (city, user_id,))
    commit()


# получание всех ID из базы TODO не оптимально
def read_all_id_from_database():
    cursor = get_cursor()
    cursor.execute('SELECT DISTINCT user_id FROM user_settings')
    result = cursor.fetchall()
    ids = []
    for x in result:
        ids.append(int(x[0]))
    commit()
    return ids


def remove_duplicates_from_list(array):
    return list(dict.fromkeys(array))


# удалить базу
'''
def drop_table():
    cursor = get_cursor()
    cursor.execute('DROP TABLE IF EXISTS user_message')
    commit()
'''

"""
# удаляем ID пользователя при выходе из бота
def delete_id_from_database(user_id: int):
    cursor = get_cursor()
    cursor.execute('INSERT INTO user_data (user_id, first_name, last_name) VALUES (?, ?, ?)', (user_id))
    commit()
"""

##Погода
# сохранять Погоду и данные пользователя
def save_user_status(user_id: int, time_data: str, current_city: str, temperature: float, real_feel: float, air_pressure: int, humidity: float, wellness_score: int, backpain_data: int, headpain_data: int):
    cursor = get_cursor()
    cursor.execute('INSERT INTO user_meteo_data (user_id, time_data, current_city, temperature, real_feel, air_pressure, humidity , wellness_score , backpain_data , headpain_data) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, time_data, current_city, temperature, real_feel, air_pressure, humidity , wellness_score , backpain_data , headpain_data))
    commit()


## прочитать Погоду и данные пользователя
# TODO  передаем в функцию id пользователя, получаем все записи за период, пака что за все дни!!!
def read_userdata_from_database(user_id: int):
    cursor = get_cursor()
    cursor.execute('SELECT * FROM user_meteo_data WHERE user_id=?', (user_id,))
    raw_data=cursor.fetchall()
    for i in raw_data:
        print(i)