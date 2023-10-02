from src.classes.JSONSaver import JSONSaver
from src.classes.Vacancy import Vacancy
from utils.utils import get_formatted_vacancies, print_sorted_vacancies, print_sorted_salary

def get_user_input(prompt: str, options=None):
    """
    Функция для получения ввода пользователя с опциональным ограничением по вариантам ответа.
    """
    while True:
        user_input = input(prompt)
        if options is None or user_input in options:
            return user_input
        else:
            print("Пожалуйста, введите корректный вариант.")


def user_interaction():
    """
    Консольный интерфейс для пользователя
    """
    vacancies_list = []

    user_input = get_user_input("Выберите платформу:\n"
                                "1. hh.ru\n"
                                "2. superjob\n"
                                "3. hh.ru и superjob\n")
    city = input("Введите свой город:\n")
    query = input("Введите название профессии:\n")
    experience = get_user_input("Выберите требуемый опыт работы:\n"
                                "1. Без опыта\n"
                                "2. От 1 до 3 лет\n"
                                "3. От 3 до 6 лет\n"
                                "4. Более 6 лет\n")

    vacancies = get_formatted_vacancies(user_input, query, city, experience)
    vacancy_objects = [Vacancy(**vac) for vac in vacancies]

    # Вывод всех вакансий
    for vac in vacancy_objects:
        print(vac)
    print()

    user_input = get_user_input("Что мне сделать?\n"
                                "1. Отсортировать вакансии по з/п.\n"
                                "2. Показать вакансии начиная с n-ой суммы\n"
                                "3. Сохранить вакансию\n")

    if user_input == "1":
        user_input = get_user_input("1. От большей к меньшей з/п\n"
                                    "2. От меньшей к большей з/п\n")
        print_sorted_vacancies(user_input, vacancy_objects)
    elif user_input == "2":
        user_input = input("Введите минимальную з/п:")
        print_sorted_salary(user_input, vacancy_objects)
    elif user_input == "3":
        file_name = "vacancies.json"
        while True:
            JSONSaver.add_vacancy(vacancies_list)
            JSONSaver.save_to_json(vacancies_list, file_name)
            user_input = get_user_input("Что мне сделать?\n"
                                        "1. Добавить вакансию.\n"
                                        "2. Выйти.\n")
            if user_input == "2":
                break
    else:
        print("Ошибка")


if __name__ == "__main__":
    user_interaction()
