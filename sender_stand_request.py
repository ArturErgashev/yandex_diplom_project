import configuration
import requests

def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track_number))