import requests


class YandexDisk:

    def __init__(self, API_TOKEN):
        self.token = API_TOKEN

    '''Создание папки'''
    def create_folder(self, name):
        URL = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": f"OAuth {self.token}", 
            "Content-Type": "application/json", 
            "Accept": "application/json",
            }
        params = {"path": f"{name}"}
        response = requests.put(URL, headers=headers, params=params)
        return response

    '''Удаление папки'''
    def delete_folder(self, name):
        URL = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": f"OAuth {self.token}", 
            "Content-Type": "application/json", 
            "Accept": "application/json",
            }
        params = {"path": f"{name}"}
        response = requests.delete(URL, headers=headers, params=params)
        return response
