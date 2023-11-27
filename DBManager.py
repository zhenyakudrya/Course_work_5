import psycopg2
from psycopg2 import Error
import os


class DBManager:
    """
    Класс для работы с БД
    """

    def __init__(self, db_name):
        self.user = "postgres"
        self.password = os.getenv('PSWRD')
        self.host = "localhost"
        self.database = db_name

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании
        """
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    database=self.database)

            cursor = conn.cursor()
            query = """SELECT employer, COUNT(*)
                       FROM vacancies
                       GROUP BY employer"""
            cursor.execute(query)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    database=self.database)

            cursor = conn.cursor()
            query = """SELECT employer, title, salary_from, url
                              FROM vacancies"""
            cursor.execute(query)
            print(cursor.fetchall())
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям
        """
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    database=self.database)

            cursor = conn.cursor()
            query = """SELECT AVG(salary_from)
                              FROM vacancies
                              WHERE salary_from > 0"""
            cursor.execute(query)
            print(cursor.fetchall())
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    database=self.database)

            cursor = conn.cursor()
            query = """SELECT title
                       FROM vacancies
                       WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies WHERE salary_from > 0)"""
            cursor.execute(query)
            print(cursor.fetchall())
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def get_vacancies_with_keyword(self, keyword):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова,
        например python
        """
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    database=self.database)

            cursor = conn.cursor()
            query = f"SELECT title FROM vacancies WHERE title LIKE %{keyword}%"
            cursor.execute(query)
            print(cursor.fetchall())
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if conn:
                cursor.close()
                conn.close()
