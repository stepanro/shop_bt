from mysql.connector import Error
import mysql.connector
import os
from config_data.config import load_dotenv

host_name = os.getenv('HOST_NAME')
user_name = os.getenv('HOST_USER_NAME')
user_password = os.getenv('PASSWORD')
database_name = os.getenv('NAME_DATABASE')


def database_connect(host_name, user_name, user_password, database_name):
    connect = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database_name
    )

    return connect


# def write_database_from_csv_file():
#     with open(file='../other_files/database.csv', mode='r', encoding='utf-8') as database:
#         with database_connect(
#                 host_name=host_name,
#                 user_name=user_name,
#                 user_password=user_password,
#                 database_name=database_name) as actual_connect:
#             for count, res_read_base in enumerate(database):
#                 cursor = actual_connect.cursor()
#                 command = """INSERT INTO `shop_tb.diapers`
#                 (`type_goods`, `age`, `size`, `vendor_code`, `name_goods`, `description`,
#                 `units`, `weight`, `quantity`, `diameter`, `color`, `price`, `path_picture`, `site_link`)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#                 if count > 0:
#                     _, _, type_goods, age, size, vendor_code, name_goods, description, units, weight, quantity, \
#                             diameter, color, price, picture, link = str(res_read_base).split(',')
#                     value = [type_goods, age, size, vendor_code, name_goods, description, units, weight, quantity,
#                              diameter, color, price, picture, link]
#                     cursor.execute(command, value)
#                     cursor.commit()
#
# write_database_from_csv_file()

