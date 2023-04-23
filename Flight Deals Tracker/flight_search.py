import requests
from datetime import datetime, timedelta
API = "h69sfTfBtL7xCpeoHkQKF0zTV3y9Vmqb"
endpoint = "https://api.tequila.kiwi.com/locations/query"
endpoint1 = "https://api.tequila.kiwi.com/v2/search"
header = {
    "apikey": API
}
today = datetime.now() + timedelta(days=1)
six_mon_later = today + timedelta(days=183)
today = today.strftime("%d/%m/%Y")
six_mon_later = six_mon_later.strftime("%d/%m/%Y")


class FlightSearch:
    def get_IATA(self, city_list: list):
        self.city_list = city_list
        self.list = []
        for i in city_list:
            query = {"term": i, "location_types": "city"}
            response = requests.get(url=endpoint, headers=header, params=query)
            results = response.json()["locations"][0]["code"]
            self.list.append(results)
        return self.list

    def search_flight(self, code_list: list):
        for i in range(0,len(code_list)):
            parameters = {
                "fly_from": "LON",
                "fly_to": code_list[i],
                "date_from": today,
                "date_to": six_mon_later,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }
            response1 = requests.get(url=endpoint1, headers=header, params=parameters)
            result = response1.json()
            cost = result["data"][0]["price"]
            date = result["data"][0]["local_departure"].split("T")
            date = date[0]
            price = {
                code_list[i]: [cost, date],
            }
            return price

