import sender_stand_request
import data

# Ольга Благова, 19-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест 1. Выполнить запрос на создание заказа и сохранение номера трека заказа
def test_create_order():
    response = sender_stand_request.post_create_order(data.order_body)
    assert response.status_code == 201
    assert response.json()["track"] > 0

# Тест 2. Выполнить запрос на получения заказа по треку заказа
def test_get_order():
    track_response = sender_stand_request.post_create_order(data.order_body)
    response = sender_stand_request.get_order(track_response.json()["track"])
    assert response.status_code == 200
    assert response.json()["order"]["track"] == track_response.json()["track"]