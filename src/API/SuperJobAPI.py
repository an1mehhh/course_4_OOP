import requests

from src.class_abstractions.AbstractionsAPI import AbstractionsAPI


class SuperJobAPI(AbstractionsAPI):

    def __init__(self):
        self.url = "https://api.superjob.ru/2.0"
        self.__TOKEN = {
            "X-Api-App-Id": "v3.r.130694942.a51a30d6f9a56fab6ddf3527baae135d70349996.813584607ae22116f8558163084dd22beaef7f75"}

    def _get_city(self, city: str) -> str:
        if len(city) == 0:
            return None
        else:
            response = requests.get(f"{self.url}/towns/").json()
            city = city.lower().title()

            for towns in response['objects']:
                if towns["title"] == city:
                    return towns["id"]

    def get_vacancies(self, search_query: str, city: str = None, experience: str = None) -> list:

        response = requests.get(f"{self.url}/vacancies",
                                params={"keyword": search_query,
                                        "town": self._get_city(city),
                                        "experience": experience},
                                headers=self.__TOKEN)
        if response.status_code == 200:
            data = response.json()
            return data.get("objects", [])
        else:
            print(f"Request failed with status code: {response.status_code}")

    def get_formatted_data_vacancies(self, search_query: str, city: str = None, experience: str = None) -> list:

        data_vacancies = self.get_vacancies(search_query, city, experience)
        vacancies = []
        for vac in data_vacancies:
            vacancies.append({
                "id": vac.get("id", "Нет данных."),
                "name": vac.get('profession', 'Нет данных.'),
                "company": vac.get('firm_name', 'Нет данных.'),
                "experience": vac.get('experience', 'Нет данных.').get('title', 'Нет данных.'),
                "city": vac.get('town', {}).get('title', 'Нет данных.'),
                "vac_url": vac.get('link'),
                "salary": {
                    "from": vac.setdefault('payment_from'),
                    "to": vac.setdefault("payment_to"),
                    "currency": vac.setdefault("currency")
                },
            })

        return vacancies