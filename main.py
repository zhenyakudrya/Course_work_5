from headhunterapi import HeadHunterAPI
from itertools import chain


employer_id_list = [39305, 64174, 3529, 193400, 2624085, 7172, 3093544, 625332, 3530, 49357]
vacancy_list = []

hh_api = HeadHunterAPI()

for employer_id in employer_id_list:
    hh_vacancies = hh_api.get_vacancies_by_id(employer_id)
    hh_standard_vacancies = hh_api.standard_vacancies(hh_vacancies)
    vacancy_list.append(hh_standard_vacancies)

#Преобразование списка
items = list(chain(*vacancy_list))
print(items)