import pyodbc
import psycopg2 as pg
from psycopg2 import Error
import sqlite3


def connect_to_postgres_db():
    try:
        # Подключение к существующей базе данных
        connection = pg.connect(user="latyn",
                                password="nytal",
                                host="10.3.3.67",
                                database="elsec")

        return connection
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL: ", error)


if __name__ == '__main__':

    sql_lite_con = sqlite3.connect('testdb.db')
    sql_lite_cursor = sql_lite_con.cursor()

    try:
        sql_lite_cursor.execute("SELECT * From Event_TU")
        rows = sql_lite_cursor.fetchall()

        for row in rows:
            key_link = row[0]
            code = row[1]
            dt = row[2]
            dtcp = row[3]
            obj = row[4]
            caption = row[5]
            comment = row[6]
            user = row[7]
            kwit = row[8]
            data = row[9]

            print(row)

    except (Exception, Error) as error:
        print("Ошибка при работе: ", error)
    finally:
        if sql_lite_con:
            sql_lite_con.close()
