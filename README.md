﻿# Автотест для диплома курса Яндекс.Практикум. Проект Яндекс.Самокат.


## Описание
URL и пути запросов хранятся в файле `configuration.py`,
данные POST-запросов в файле `Data.py`.

Отправка запросов в файле `sender_standart_request.py` содержит функции:
- `create_order` - отправляет запрос на создание заказа и возвращает трек-номер для данного заказа;
- `get_order_by_track_number` - отправляет запрос на получение информации о заказе
по его трек-номеру и возвращает информацию о заказе.

Тест находится в файле `get_track_orders_test.py`
Тест `test_order_creation_and_receiving` на проверку создания нового заказа и 
получения информации о нём по его трек-номеру.


## Запуск тестов
- Для запуска тестов должны быть установлены пакеты `pytest` и `requests`.
- Для запуска теста необходимо подставить действующую ссылку на сервер приложения Яндекс Самокат в файле 
`configuration.py`, в поле `URL_SERVICE`
- Запуск всех тестов осуществляется через конфигурацию `test_run`