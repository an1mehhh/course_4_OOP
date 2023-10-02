import json
import os

from src.classes.Vacancy import Vacancy


class JSONSaver:

    @staticmethod
    def add_vacancy(vacancies_list: list):
        """
        Добавляет вакансию в список вакансий.
        """
        name = input("Введите название вакансии: ")
        while True:
            try:
                salary_from = int(input("Введите зарплату 'от': "))
                salary_to = int(input("Введите зарплату 'до': "))
                break
            except ValueError:
                print("Пожалуйста, введите корректное число для зарплаты.")

        currency = input("Введите валюту: ")
        employer = input("Введите название компании: ")
        vac_url = input("Введите URL вакансии: ")

        new_vacancy = Vacancy(name, {"from": salary_from, "to": salary_to, "currency": currency}, employer, vac_url)
        vacancies_list.append(new_vacancy)

        print(f"Вакансия '{name}' успешно добавлена!")
        return new_vacancy

    @staticmethod
    def save_to_json(vacancies_list: list, filename: str):
        """
        Сохраняет список вакансий в JSON файл.
        """
        if os.path.exists(filename):
            response = input(f"Файл '{filename}' уже существует. Хотите перезаписать его? (y/n): ")
            if response.lower() != 'y':
                print("Отмена сохранения.")
                return

        # Сохраняем список вакансий в JSON файл
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([vacancy.to_dict() for vacancy in vacancies_list], file, indent=2, ensure_ascii=False)
