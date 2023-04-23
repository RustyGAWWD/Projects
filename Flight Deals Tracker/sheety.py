sheety_api = "https://api.sheety.co/6f2d1b5744dc3bd56d7c863c8a373aa3/flightDeals/prices"
import requests
class Sheety:
    def get_city_list(self):
        response = requests.get(url=sheety_api)
        response.raise_for_status()
        self.sheet_data = response.json()
        city_list = []
        for i in range(0, len(self.sheet_data["prices"])):
            city_list.append(self.sheet_data["prices"][i]["city"])
        return city_list

    def update_code(self, code_list: list):
        for i in range(0, len(self.sheet_data["prices"])):
            new_data = {
                "price": {
                    "iataCode": code_list[i]
                }
            }
            response = requests.put(
                url=f'{sheety_api}/{self.sheet_data["prices"][i]["id"]}',
                json=new_data
            )

