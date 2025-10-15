import requests
from pprint import pprint

endpoint = "http://127.0.0.1:8000/profils-api-view/3/"

data = {
    "nom": "Le fils",
    "prenom": "heroyinus",
    "article": "KATANA pour le petit",
    "montant": 76587
    
                        
}

response = requests.patch(endpoint, json=data)
pprint(response.json())
print(response.status_code)
    