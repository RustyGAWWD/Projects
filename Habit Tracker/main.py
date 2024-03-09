import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "rustygawwd"
token = "31100511"

user_params = {
    "token": "31100511",
    "username": "rustygawwd",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "nofap",
    "unit": "days",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": token
}

today = datetime(year=2023, month=3, day=3)

graph_response = requests.post(graph_endpoint, json=graph_parameters, headers=headers)

progress_input_endpoint = f'{graph_endpoint}/graph1/{today.strftime("%Y%m%d")}'

progress_input_parameters = {
    # "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

progress_input_response = requests.delete(url=progress_input_endpoint, headers=headers)
print(progress_input_response.text)