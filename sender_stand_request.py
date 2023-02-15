import configuration
import requests
import data

def post_new_order(data): # создаём новый заказ, который содержит токен Authorization
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDER,  # url + api запрос на создание пользоваетеля
                         json = data.user_order)  # указываем тело

response = post_new_order(data)

print (response.json())

def get_an_order_track(): #функция на получение заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_TRACK,
                        params={"t":response.json()['track']})
response2 = get_an_order_track()
print (response2.json())