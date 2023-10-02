from src.classes.VacancyFilter import VacancyFilter
from src.API.HeadHunterAPI import HeadHunterAPI
from src.API.SuperJobAPI import SuperJobAPI


def get_data(user_input, query, city, experience):
    """Выбор API"""
    managers = []

    if user_input == "1":
        managers = [HeadHunterAPI()]
    elif user_input == "2":
        managers = [SuperJobAPI()]
    elif user_input == "3":
        managers = [HeadHunterAPI(), SuperJobAPI()]
    vacancies = []
    for manager in managers:
        vacancies += manager.get_formatted_data_vacancies(query, city, experience)

    return vacancies


def get_formatted_vacancies(user_input: str, query: str, city: str, experience: str) -> list:
    """Обработка данных """
    vacancies = get_data(user_input, query, city, experience)
    formatted_vacancies = [{"name": vac['name'],
                            "salary": vac["salary"],
                            "employer": vac["company"],
                            "vac_url": vac["vac_url"]} for vac in vacancies]

    return formatted_vacancies


def print_sorted_vacancies(user_input: str, vacancy_objects: list):
    """сортировка вакансий"""

    if user_input == "1":
        sorted_vacancies = VacancyFilter.sort_by_salary(vacancy_objects, True)
        for vac in sorted_vacancies:
            print(vac)
    elif user_input == "2":
        sorted_vacancies = VacancyFilter.sort_by_salary(vacancy_objects, False)
        for vac in sorted_vacancies:
            print(vac)


def print_sorted_salary(user_input: str, vacancy_objects: list):
    """вакансии по минимальной зарплате"""
    filtered_vacancies = VacancyFilter.filter_by_salary(vacancy_objects, int(user_input))
    for vac in filtered_vacancies:
        print(vac)
