import sender_stand_request # импортируем данные о заказе и треке
def test_proverka_code_200():
    right_check= sender_stand_request.response2
    assert right_check.status_code==200
