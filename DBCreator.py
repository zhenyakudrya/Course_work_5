import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
import os


class DBCreator:
    """
    Класс для создания БД
    """

    def __init__(self):
        self.user = "postgres"
        self.password = os.getenv('PSWRD')
        self.host = "localhost"

    def create_db(self, db_name):
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            sql_create_database = f"create database {db_name}"
            cursor.execute(sql_create_database)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def create_table(self, db_name, table_name):
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    database=f"{db_name}")
            cursor = conn.cursor()
            create_table_query = """ CREATE TABLE """f'{table_name}'"""
                                     (
                                         title text,
                                         url text,
                                         salary_from int,
                                         employer text,
                                         employer_id int
                                     )"""
            cursor.execute(create_table_query)
            conn.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
        pass

    def fill_table(self, db_name, vacancies_list):
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    database=f"{db_name}")

            cursor = conn.cursor()
            for vacancy in vacancies_list:
                cursor.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)",
                               (vacancy["title"], vacancy["url"], vacancy["salary_from"],
                                vacancy["employer"], vacancy["employer_id"]))
            conn.commit()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
