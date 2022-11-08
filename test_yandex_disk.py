import random
import string

from yandex_disk import YandexDisk
from settings import API_TOKEN

'''
Удаление папки с таким же названием, если она существует
Создание новой папки
Проверка кода на соответствие требованию
Проверка тела ответа на соответствие требованию
Удаление созданной папки по завершению теста
'''
class TestFolderCreation:

    NAME = ''.join(random.sample(string.ascii_lowercase, 8))

    def setup_method(self):
        self.login = YandexDisk(API_TOKEN)
        self.login.delete_folder(self.NAME)

    def teardown_method(self):
         self.login.delete_folder(self.NAME)

    def test_create_folder(self):
        response = self.login.create_folder(self.NAME)
        path = self.login.info(self.NAME)["_embedded"]["path"]
        print(path)
        assert response.status_code == 201, "Ошибка создания папки"
        assert path == f"disk:/{self.NAME}", "Папка не была создана"
