import time
import requests
from pprint import pprint
# ----красиво забираем токен из вложенного файла--------
with open("token.txt", "r") as file_object:
    token = file_object.read().strip()

def search_groups(q, sorting=0):
    params = {
        "q": q,
        "access_token": token,
        "v": "5.131",
        "sort": sorting,
        "count": 10
    }
    req = requests.get("https://api.vk.com/method/groups.search", params).json()
    req = req["response"]["items"]
    return req

target_groups = search_groups("python")

pprint(target_groups)