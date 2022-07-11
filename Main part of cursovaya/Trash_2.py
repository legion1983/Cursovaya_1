import requests
from pprint import pprint
with open("token.txt", "r") as file_object:
    token = file_object.read().strip()

class VkUser:
    url = "https://api.vk.com/method/"
    def __init__(self, token, version):
        self.params = {
            "access_token": token,
            "v": version
        }


    def search_groups(self, q, sorting=0):
        group_search_url = self.url + "groups.search"
        group_search_params = {
            "q": q,
            "sort": sorting,
            "count": 300
        }
       # -----------------------------склеил 2ва словаря тут------------------------------
        req = requests.get(group_search_url, params={**self.params, **group_search_params}).json()
        return req["response"]["items"]
