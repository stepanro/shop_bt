from mysql.connector import Error
import mysql
import os
from config_data.config import load_dotenv

host_name = os.getenv('HOST_NAME')
user_name = os.getenv('HOST_USER_NAME')
user_password = os.getenv('PASSWORD')
database_name = os.getenv('NAME_DATABASE')


class DatabaseConnectionSingleton:
    """ Класс синглтон, создает подключение к базе дынных, и пока объект создан, возвращает его же. """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                database=database_name
            )

        return cls.__instance


def get_type_goods() -> tuple:
    """ Функция запрашивает из базы данных список уникальных типов
    товара, и возвращает картеж состоящий из этих типов"""
    actual_connect = DatabaseConnectionSingleton()
    cursor = actual_connect.cursor()
    command = """SELECT DISTINCT `type_goods` FROM `diapers`"""
    type_goods = list()
    cursor.execute(command)

    for res_type_goods in cursor.fetchall():
        type_goods.append(res_type_goods[0])

    return tuple(type_goods)


def get_age(type_goods) -> tuple:
    """ Функция запрашивает из базы данных список уникальных типов возрастов,
     и возвращает картеж состояний из этих типов """
    actual_connect = DatabaseConnectionSingleton()
    cursor = actual_connect.cursor()
    command = """SELECT DISTINCT `age` FROM `diapers` WHERE `type_goods` = '{type_goods}' """.format(type_goods=type_goods)
    type_age = list()
    cursor.execute(command)

    for res_age in cursor.fetchall():
        type_age.append(res_age[0])

    return tuple(type_age)


def get_size(type_goods, type_age) -> tuple:
    """ Функция запрашивает из базы данных список уникальных типов размеров,
     и возвращает картеж состояний из этих типов """
    actual_connect = DatabaseConnectionSingleton()
    cursor = actual_connect.cursor()
    command = """SELECT DISTINCT `size` FROM `diapers` WHERE `type_goods` = '{type_goods}' AND `age` = '{age}' """.format(type_goods=type_goods, age=type_age)
    type_size = list()
    cursor.execute(command)

    for res_size in cursor.fetchall():
        type_size.append(res_size[0])

    return tuple(type_size)


def get_number_validate_goods(type_goods, type_age, type_size):
    """ Функция запрашивает из базы данных количество валидных товаов """
    actual_connect = DatabaseConnectionSingleton()
    cursor = actual_connect.cursor()
    command = """SELECT COUNT(*) FROM `diapers` WHERE `type_goods` = '{type_goods}' AND `age` = '{age}' AND `size` = '{type_size}' """.format(type_goods=type_goods, age=type_age, type_size=type_size)
    count_results = list()
    cursor.execute(command)

    for res_count in cursor.fetchall():
        count_results.append(res_count[0])

    return tuple(count_results)


def get_results(type_goods, type_age, type_size):
    """ Функция запрашивает из базы данных валидные товары """
    actual_connect = DatabaseConnectionSingleton()
    cursor = actual_connect.cursor()
    command = """SELECT `id`, `name_goods`, `vendor_code` FROM `diapers` WHERE `type_goods` = '{type_goods}' AND `age` = '{age}' AND `size` = '{type_size}' """.format(type_goods=type_goods, age=type_age, type_size=type_size)
    count_results = list()
    cursor.execute(command)

    for id, name_goods, vendor_code in cursor.fetchall():
        count_results.append((id, name_goods, vendor_code))

    return tuple(count_results)

