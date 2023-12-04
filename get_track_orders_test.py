import sender_standart_request
import Data


# Евгений Бойцов, 11-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест на создание и получения заказа по трек-номеру.
def test_order_creation_and_receiving():
    track_number = sender_standart_request.create_order(Data.order_body)

    response = sender_standart_request.get_order_by_track_number(track_number)
    assert response.status_code == 200
