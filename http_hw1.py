from pprint import pprint
import ast

import requests

TOKEN = "3018687491722745"

def test_request():
    name = ["Hulk","Captain America","Thanos"]
    url = "https://superheroapi.com/api/"
    key = TOKEN
    file = open("1.txt", "w")
    for i in name:
        search = f"/search/{i}"
        endpoint_url =f"{url}{key}{search}"
        response = requests.get(endpoint_url,  timeout = 5)
        pprint(response.text)
        file.write(response.text + "\n")



test_request()
def get_hero_int():

    with open("1.txt", "r", encoding="utf8") as file:
        for i in file:


    # for i in file :
    #
    #     for each in ingredients:
    #         name = each["Ingredient name"]
    #
    #         quantity = each["Quantity"]
    #
    #         measure = each["Measure"][0]
    #
    #         result[name] ={"Quantity": int(quantity)*person_count, "Measure": measure}
    # return result
