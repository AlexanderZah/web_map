# Тестовое задание.
Веб-приложение для отображения карты Нижнего Новгорода.
https://alexanderzah.pythonanywhere.com/
# Функционал:
- Изменение слоя карты.
  - Схема;
  - Рельеф;
  - Спутник.
- Скрытие/отображение группы элементов.
  - Достопримечательности;
  - Сбер;
  - Парки;
- Определение местоположения пользователя.

# Директории:
- Настройки проекта - config
- Обработка запросов, отображение карты - web_map
- логика построенаия карты - service_map
- тесты построения карты - tests_service_map

# Установка:
1) Склонировать репозиторий.
```
git clone https://github.com/AlexanderZah/web_map.git && cd web_map
```
2) Создать виртуалную среду и установить зависимости. 
```
virtualenv venv --python=3.10.5 && source venv/bin/activate
```
```
pip install -r requirements.txt
```
3) В корне проекта создать файл .env , добавить SECRET_KEY, ALLOWED_HOSTS, DEBUG.
4) Собрать статику.
```
python3 manage.py collectstatic
```
5) Запустить сервер.
```
python3 manage.py runserver
```
 
