import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
import csv
import os


class DBCreator:
    """
    Класс для создания БД
    """

    def __init__(self):
        pass

    def create_db(self):

        try:
            conn = psycopg2.connect(user="postgres",
                                    password=os.getenv('PSWRD'),
                                    host="localhost")
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            sql_create_database = 'create database vacancies_db'
            cursor.execute(sql_create_database)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def create_table(self):
        try:
            conn = psycopg2.connect(user="postgres",
                                    password=os.getenv('PSWRD'),
                                    host="localhost",
                                    database="vacancies_db")
            cursor = conn.cursor()
            create_table_query = """ CREATE TABLE vacancies
                                     (
                                         title text,
                                         url text,
                                         salary_from int,
                                         employer text,
                                         employer_id int
                                     );"""
            cursor.execute(create_table_query)
            conn.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
        pass

    def fill_table(self):
        try:
            conn = psycopg2.connect(user="postgres",
                                    password=os.getenv('PSWRD'),
                                    host="localhost",
                                    database="vacancies_db")

            cursor = conn.cursor()
            # Список вакансий
            for vac in vac_list:
                cursor.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)",
                               (vac["title"], vac["url"], vac["salary_from"], vac["employer"], vac["employer_id"]))
            conn.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
