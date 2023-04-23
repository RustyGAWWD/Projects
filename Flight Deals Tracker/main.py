
from flight_search import FlightSearch
from sheety import Sheety
from notification_manager import NotificationManager

fs = FlightSearch()
sh = Sheety()
nm = NotificationManager()

city_list = sh.get_city_list()
code_list = fs.get_IATA(city_list)
sh.update_code(code_list)
price_list = fs.search_flight(code_list)
for i in range(0, len(price_list)):
    if sh.sheet_data["prices"][i]["lowestPrice"]>price_list[code_list[i]][0]:
        nm.send_alert(sh.sheet_data["prices"][i]["city"],price_list[code_list[i]][0],price_list[code_list[i]][1])
