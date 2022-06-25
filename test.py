import requests

response = requests.get('https://rickandmortyapi.com/api/character').json()


print(response['results'])