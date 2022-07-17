import urllib.request
import requests
from pprint import pprint
with open("token.txt", "r") as file_object:
    token = file_object.read().strip()

# Чтобы обратиться к методу API ВКонтакте, нужно выполнить POST или GET запрос вида:
# https://api.vk.com/method/METHOD?PARAMS&access_token=TOKEN&v=V
# инструкция: https://dev.vk.com/api/api-requests
# базовая ссылка запроса к API VK = https://api.vk.com/method/METHOD?PARAMS&access_token=TOKEN&v=V
# METHOD?  возьмем = users.get
# PARAMS =
# access_token=TOKEN
# v=V

# _____________________________
class VkPhotoes:
    url = "https://api.vk.com/method/"
    def __init__(self, token, version):
        self.params = {
            "access_token": token,
            "v": version
        }

    def get_photoes(self, count):
        photoes_url = self.url + "photos.get"
        photoes_params = {
            "album_id": "profile",
            "owner_id": "5",
            "extended": "1",
            "count": count,
            "photo_sizes": 0
        }
        res = requests.get(photoes_url, params={**self.params, **photoes_params}).json()
        return res["response"]

vk_client = VkPhotoes(token, "5.131")
pprint(vk_client.get_photoes(count=22))

raw_date_json = vk_client.get_photoes(count=22)


picture_list_size = []
picture_list_id = []
picture_list_url = []
picture_list_likes = []

for values in raw_date_json["items"]:
    for items in values["sizes"]:
        picture_size = items['width'] * items['height']
        picture_id = values["id"]
        picture_url = items["url"]
        picture_likes = (values["likes"]["count"])
        picture_list_size += [picture_size]
        picture_list_id += [picture_id]
        picture_list_url += [picture_url]
        picture_list_likes += [picture_likes]
        sort_picture_list_size = sorted(picture_list_size)
        top_5_size_sort_picture_list_size = sort_picture_list_size[-5:]

list_max_size_position = []
for numbers in top_5_size_sort_picture_list_size:
    if numbers in picture_list_size:
        x = [picture_list_size.index(numbers)]
        list_max_size_position.extend(x)
# print("Индексы  фотографий с наибольшим размером в списке фотографий", list_max_size_position)

picture_dict_max = {}

list_final_name_additional = []
list_final_url = []
list_final_name_1st = []

for values in list_max_size_position:
    file_name_additional = picture_list_id[values]
    file_url = picture_list_url[values]
    file_name_1st = picture_list_likes[values]

    list_final_name_additional.append(file_name_additional)
    list_final_url.append(file_url)
    list_final_name_1st.append(file_name_1st)

# __________Создание словаря с 5ю файлами фотографии наибольшого размера______________________

def file_name_creation():
    final_dict = {}

    file_name_1 = list_final_name_1st[0]
    file_name_2 = list_final_name_1st[1]
    file_name_3 = list_final_name_1st[2]
    file_name_4 = list_final_name_1st[3]
    file_name_5 = list_final_name_1st[4]

    file_name_additional_1 = list_final_name_additional[0]
    file_name_additional_2 = list_final_name_additional[1]
    file_name_additional_3 = list_final_name_additional[2]
    file_name_additional_4 = list_final_name_additional[3]
    file_name_additional_5 = list_final_name_additional[4]

    list_final_url_1 = list_final_url[0]
    list_final_url_2 = list_final_url[1]
    list_final_url_3 = list_final_url[2]
    list_final_url_4 = list_final_url[3]
    list_final_url_5 = list_final_url[4]

    if file_name_1 == file_name_2 or file_name_1 == file_name_3 or file_name_1 == file_name_4 or file_name_1 == file_name_5:
        file_name_1 = str(file_name_1) + str("_") + str(file_name_additional_1)
    else:
        file_name_1 = str(file_name_1)

    if file_name_2 == file_name_1 or file_name_2 == file_name_3 or file_name_2 == file_name_4 or file_name_2 == file_name_5:
        file_name_2 = str(file_name_2) + str("_") + str(file_name_additional_2)
    else:
        file_name_2 = str(file_name_2)

    if file_name_3 == file_name_1 or file_name_3 == file_name_2 or file_name_3 == file_name_4 or file_name_3 == file_name_5:
        file_name_3 = str(file_name_3) + str("_") + str(file_name_additional_3)
    else:
        file_name_3 = str(file_name_3)

    if file_name_4 == file_name_1 or file_name_4 == file_name_2 or file_name_4 == file_name_3 or file_name_4 == file_name_5:
        file_name_4 = str(file_name_4) + str("_") + str(file_name_additional_4)
    else:
        file_name_4 = str(file_name_4)

    if file_name_5 == file_name_1 or file_name_5 == file_name_2 or file_name_5 == file_name_3 or file_name_5 == file_name_4:
        file_name_5 = str(file_name_5) + str("_") + str(file_name_additional_5)
    else:
        file_name_5 = str(file_name_5)

    final_dict["file_1"] = [file_name_1, list_final_url_1]
    final_dict["file_2"] = [file_name_2, list_final_url_2]
    final_dict["file_3"] = [file_name_3, list_final_url_3]
    final_dict["file_4"] = [file_name_4, list_final_url_4]
    final_dict["file_5"] = [file_name_5, list_final_url_5]
    pprint(final_dict)
    return final_dict
file_name_creation()


# __________Загрузка файлов на локальный диск______________________
url = link_1 = (file_name_creation()['file_1'][1])
url_picture_1 = str(file_name_creation()['file_1'][0])
urllib.request.urlretrieve(url, 'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_1 + ".jpg")

url = link_2 = (file_name_creation()['file_2'][1])
url_picture_2 = str(file_name_creation()['file_2'][0])
urllib.request.urlretrieve(url, 'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_2 + ".jpg")

url = link_3 = (file_name_creation()['file_3'][1])
url_picture_3 = str(file_name_creation()['file_3'][0])
urllib.request.urlretrieve(url, 'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_3 + ".jpg")

url = link_4 = (file_name_creation()['file_4'][1])
url_picture_4 = str(file_name_creation()['file_4'][0])
urllib.request.urlretrieve(url, 'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_4 + ".jpg")

url = link_5 = (file_name_creation()['file_5'][1])
url_picture_5 = str(file_name_creation()['file_5'][0])
urllib.request.urlretrieve(url, 'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_5 + ".jpg")

#__________Загрузка файлов на yandex диск______________________

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = "AQAAAAAAGUQeAADLW859Tk4gikBEmkURmI0u8H0"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)

create_folder('Cursovaya')

def upload_file(loadfile, savefile, replace=False):
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)

upload_file(r'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_1 + ".jpg", "VK_cursovaya/" + url_picture_1)
upload_file(r'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_2 + ".jpg", "VK_cursovaya/" + url_picture_2)
upload_file(r'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_3 + ".jpg", "VK_cursovaya/" + url_picture_3)
upload_file(r'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_4 + ".jpg", "VK_cursovaya/" + url_picture_4)
upload_file(r'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + url_picture_5 + ".jpg", "VK_cursovaya/" + url_picture_5)