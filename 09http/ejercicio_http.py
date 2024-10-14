import requests

pokemon = input("Dime el nombre o numero de pokedex de tu pokemon:").lower()

response = requests.get("https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if response.status_code == 200:
    print(response.text)
    data = response.json()
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["heigh"])
    print("Tipo(s): ")