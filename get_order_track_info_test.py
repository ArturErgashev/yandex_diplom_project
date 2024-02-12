# Эргашев Артур, 13 когорта, финальный проект (инженер по тестированию плюс)
import sender_stand_request
import data

def test_get_order_success_response_code():
    response = sender_stand_request.create_new_order(data.order_body)
    return response.json()["track"]

    track_number = response.json()["track"]

    order_response = sender_stand_request.get_order(track_number)

    assert order_response.status_code == 200
