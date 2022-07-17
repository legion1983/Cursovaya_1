import time
import requests
from pprint import pprint

# базовая ссылка запроса к API VK = https://api.vk.com/method/METHOD?PARAMS&access_token=TOKEN&v=V
# METHOD?  возьмем = users.get
# PARAMS =
# access_token=TOKEN
# v=V
token = "vk1.a.xEZKDiME4i_7ZsMZ_bUwatA86T-dkfJEIHe2FO00ghuRxEbcXcZmq6_pnYJ7WjYSrhfvEux9dYBv5XvaQOuDrP0yqaxLvpXcSQpDjhMthZucETMNd4spbvHA7c84V89pQ2jRR1Z2OomojGKGReFyz5vsBnNK1gb61DvqalBLjm_aZ-N3yKw4-EBNyGjcBalr"
URL = "https://api.vk.com/method/users.get"
params = {
    "user_ids": "1, 2",
    "access_token": token,
    "v": "5.131",
    "fields": "education,sex"
}

res = requests.get(URL, params=params)
pprint(res.json())


