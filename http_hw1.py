from pprint import pprint
import ast
import re
import json

import requests

TOKEN = "3018687491722745"

class Superhero:
    def __init__(self,name,intelligence):
        self.name = name
        self.intelligence = intelligence
hero_intel = []


def compare(heroes):
    max_int = 0
    hero_name = ""
    for hero in heroes:
        if int(hero.intelligence) > max_int:
            max_int = int(hero.intelligence)
            hero_name = hero.name
    pprint(hero_name)

def get_hero_int(intel_data):
    overall_data = json.loads(intel_data)
    name = overall_data["results-for"]
    intelligence = overall_data["results"][0]["powerstats"]["intelligence"]
    hero = Superhero(name, intelligence)
    hero_intel.append(hero)


def test_request():
    name = ["Hulk","Captain America","Thanos"]
    url = "https://superheroapi.com/api/"
    key = TOKEN
    for i in name:
        search = f"/search/{i}"
        endpoint_url =f"{url}{key}{search}"
        response = requests.get(endpoint_url,  timeout = 5)
        get_hero_int(response.text)
    compare(hero_intel)




test_request()













