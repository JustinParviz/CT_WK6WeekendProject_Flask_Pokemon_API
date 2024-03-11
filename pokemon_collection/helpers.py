import requests

def get_pokemon_info(pokemon):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    print(r.status_code)
    if r.status_code == 200:
        data = r.json()

        
        id = data ['id']
        name = data['name']
        description = [f"This pokemon can do {pokemove['move']['name']}" for pokemove in data['moves']]
        image = data['sprites']['front_shiny']
        type = [type_['type']['name'] for type_ in data['types']]
        ability = [pokebility['ability']['name'] for pokebility in data['abilities']]
        weight = data['weight']
        height = data['height']

        poke = {
            "name": name,
            "id": id,
            "description": description,
            "image": image,
            "type": type,
            "ability": ability,
            "weight": weight,
            "height": height
        }

        return poke
    



