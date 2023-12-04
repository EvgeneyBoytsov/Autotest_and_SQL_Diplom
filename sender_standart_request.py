import configuration
import requests


# Функция отправки запроса на создание заказа.
# Возвращаемое значение: трек-номер для созданного заказа.
def create_order(body):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDERS
    response = requests.post(url, json=body)
    track_number = response.json()["track"]
    return track_number


# Функция отправки запроса на получение заказа по его трек-номеру.
# Возвращаемое значение: ответ на запрос с информацией о заказе.
def get_order_by_track_number(track_number):
    url = f"{configuration.URL_SERVICE}/v1/orders/track?t={track_number}"
    response = requests.get(url)
    return response
