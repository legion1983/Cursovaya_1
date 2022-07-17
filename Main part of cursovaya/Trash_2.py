import pandas as pd

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

    def search_groups_ext(self, q, sorting=0):
        group_search_ext_url = self.url + "groups.getById"
        target_groups = self.search_groups(q, sorting)
        target_group_ids = ",".join([str(group["id"]) for group in target_groups])
        groups_info_params = {
            "group_ids": target_group_ids,
            "fields": "member_count, activity, description"
            }
        req = requests.get(group_search_ext_url, params={**self.params, **groups_info_params}).json()
        return req["response"]

    def get_followers(self, user_id=None):
        followers_url = self.url + "users.getFollowers"
        followers_params = {
            "count": 1000,
            "user_id": user_id
        }
        res = requests.get(followers_url, params={**self.params, **followers_params}).json()
        return res["response"]

vk_client = VkUser(token, "5.131")
# pprint(vk_client.search_groups("python"))
# pprint(vk_client.search_groups_ext("python"))
pprint(vk_client.get_followers(1))

# pd.DataFrame(vk_client.search_groups_ext("python"))
