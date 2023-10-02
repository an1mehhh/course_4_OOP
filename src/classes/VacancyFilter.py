class VacancyFilter:
    @staticmethod
    def sort_by_salary(vacancies: list, reverse: bool) -> list:
        """сортировка вакансий"""
        sorted_vacancies = sorted(
            vacancies,
            key=lambda x: x.salary.get('from', 0) if x.salary else 0,
            reverse=reverse
        )
        return sorted_vacancies

    @staticmethod
    def filter_by_salary(vacancies: list, min_salary: int):
        """Сортировка от минимальной з/п"""
        filtered_vacancies = [vacancy for vacancy in vacancies if
                              vacancy.salary and vacancy.salary.get('from', 0) >= min_salary]
        return filtered_vacancies
