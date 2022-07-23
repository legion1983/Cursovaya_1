import json
import urllib.request
import requests
from pprint import pprint

with open("token.txt", "r") as file_object:
    token = file_object.read().strip()


# _________делаем запрос к api и вынимаем всю информацию_______
class VkPhotoes:
    url = "https://api.vk.com/method/"

    def __init__(self, token, version):
        self.params = {
            "access_token": token,
            "v": version
        }

    def get_photoes(self, count, q_ty_of_photos_max_size):
        photoes_url = self.url + "photos.get"
        photoes_params = {
            "album_id": "profile",
            "owner_id": "5",
            "extended": "1",
            "count": count,
            "photo_sizes": 0
        }
        res = requests.get(photoes_url, params={**self.params, **photoes_params}).json()
        dict_short = {}

# создаем специальный словарь dict_short, который сожержит только важную информацию о фотографиях (size, id, likes)
        picture_list_size = []
        picture_list_url = []
        picture_list_date = []
        picture_list_likes = []
        picture_file_names = 'None'
        for values in res["response"]["items"]:
            # pprint(values)
            for picture_size_date in values["sizes"]:
                picture_list_size.append(picture_size_date['width'] * picture_size_date['height'])
                picture_list_url.append(picture_size_date['url'])
                length = len(picture_list_size)
                if picture_size_date["url"] in picture_list_url:
                    picture_list_date.append(values['date'])
                    picture_list_likes.append(values['likes']["count"])
                for z in range(0, length):
                    dict_short[z] = dict(size=picture_list_size[z], date=picture_list_date[z], likes=picture_list_likes[z], file_names=picture_file_names, url=picture_list_url[z])
        # pprint(dict_short)

# ищем через сортировку фотографии с максимальным размером и их позиционный номер в нашем специальном словаре dict_short
        list_max_size_pictures = []
        for values in dict_short.values():
            list_max_size_pictures.append((values['size']))
        list_max_size_pictures_sorted = sorted(list_max_size_pictures)[-q_ty_of_photos_max_size:]
        # print(list_max_size_pictures)

        list_max_size_pictures_url = []
        for values in dict_short.values():
            for items in values.values():
                if items in list_max_size_pictures_sorted:
                    list_max_size_pictures_url.append(values['url'])

# оставляет в словаре только значения с минимальными размерами фотографий
        new_dict = {}
        for key, value in dict_short.items():
            if value["url"] in list_max_size_pictures_url:
                new_dict[key] = value
        # pprint(new_dict)

        picture_names_for_new_dict = []
        picture_date_new_dict = []

        for values in new_dict.values():
            picture_names_for_new_dict.append(values["likes"])
            picture_date_new_dict.append(values["date"])

# меняет имена фотографий, если они имеют одинаковое количество лайков
        unique_names = []
        unique_indexes = []
        for number in picture_names_for_new_dict:
            if number not in unique_names:
                unique_names.append(number)
            else:
                unique_names.append(str(picture_names_for_new_dict[picture_names_for_new_dict.index(number)]) + "." + str(picture_date_new_dict[picture_names_for_new_dict.index(number)]))
        # print(unique_names)
        return [new_dict, unique_names]


vk_client = VkPhotoes(token, "5.131")
urls = vk_client.get_photoes(count=11, q_ty_of_photos_max_size=5)
pprint(urls)

# ___________________________сохраняем информацию о файле в json формат_____________________
with open('data.txt', 'w', encoding='utf-8') as f:
    json.dump(vk_client.get_photoes(count=11, q_ty_of_photos_max_size=5), f, ensure_ascii=False, indent=4)

# __________Загрузка файлов на локальный диск______________________
def uploading_files():
    lenght = len(urls[0].values())
    url_list = []
    for values in urls[0].values():
        url = values["url"]
        url_list.append(url)
    for i in range(0, lenght):
        picture_file_name = urls[1][i]
        urllib.request.urlretrieve(url_list[i], 'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + str(picture_file_name) + ".jpg")
uploading_files()

# __________Загрузка файлов на yandex диск______________________
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = "AQAAAAAAGUQeAADLW859Tk4gikBEmkURmI0u8H0"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)
create_folder('VK_cursovaya')

def upload_file(loadfile, savefile, replace=False):
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)

lenght = len(urls[0].values())
for i in range(0, lenght):
    picture_file_name = urls[1][i]
    print(urls[1][i])
    upload_file(r'C:/Users/daria/OneDrive/Рабочий стол/Нетология/cursovaya/' + str(picture_file_name) + ".jpg", "VK_cursovaya/" + str(picture_file_name))