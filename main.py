from headhunterapi import HeadHunterAPI
from DBCreator import DBCreator
from DBManager import DBManager
from itertools import chain


def main():
    # Список id работодателей на HeadHunter
    employer_id_list = [39305, 64174, 3529, 193400, 2624085, 7172, 3093544, 625332, 3530, 49357]
    # Список вакансий от всех работодателей
    vacancies_list = []

    # Создание экземпляра класса HeadHunterAPI для работы с API
    hh_api = HeadHunterAPI()

    # Получение списка данных по вакансиям
    for employer_id in employer_id_list:
        hh_vacancies = hh_api.get_vacancies_by_id(employer_id)
        hh_standard_vacancies = hh_api.standard_vacancies(hh_vacancies)
        vacancies_list.append(hh_standard_vacancies)

    # Преобразование списка
    vacancies_list = list(chain(*vacancies_list))

    # Создание экземпляра класса DBCreator для создание БД и таблицы
    db_creator = DBCreator()

    # Создание базы данных
    db_creator.create_db('vacancies_db')

    # Создание таблицы
    db_creator.create_table('vacancies_db', 'vacancies')

    # Заполнение таблицы данными из списка
    db_creator.fill_table('vacancies_db', vacancies_list)

    # Создание экземпляра класса DBManager
    db_manager = DBManager('vacancies_db')

    # Исполнение SQL запросов
    db_manager.get_companies_and_vacancies_count()
    db_manager.get_all_vacancies()
    db_manager.get_avg_salary()
    db_manager.get_vacancies_with_higher_salary()
    db_manager.get_vacancies_with_keyword('спец')


if __name__ == '__main__':
    main()