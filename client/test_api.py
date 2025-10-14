import requests
from pprint import pprint

endpoint = "http://127.0.0.1:8000/my-first-api/"

data = {
    "nom": "La fillette",
    "prenom": "heroyinusta",
    "article": "Cap de super pouvoir de laser  de miel",
    "montant": 200000
                                
}

response = requests.post(endpoint, json=data)
print(response.json())
print(response.status_code)
    