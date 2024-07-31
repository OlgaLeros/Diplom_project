import configuration
import requests
import data

#Запрос на создание заказа
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

#Запрос на получения заказа по треку заказа
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))

