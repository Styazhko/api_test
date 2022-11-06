# Тестовое задание api
## Установка и запуск
1. Склонировать репозиторий с Github:
````
git clone https://github.com/Styazhko/api_test
````
2. Перейти в директорию проекта
3. Создать виртуальное окружение:
````
python -m venv venv
````
4. Активировать окружение: 
````
venv\Scripts\activate
````
5. Установка зависимостей:
```
pip install -r requirements.txt
```
6. Добавить токен в файл 'settings.py' (уже находится там)
7. Запустить тест:
```
pytest test_yandex_disk.py
```