import sender_stand_request # импортируем данные пользователя и токен Authorization + набор с сгенерированным токеном из sender_stand_request (тесты запускаются независимо по отдельности и так)

def test_proverka_code_200():
    right_check= sender_stand_request.response2
    assert right_check.status_code==200