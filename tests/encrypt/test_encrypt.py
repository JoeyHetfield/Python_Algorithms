from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # caso os valores sejam errados, chave ou mensagem

    with pytest.raises(TypeError):
        encrypt_message(1, 2)

    with pytest.raises(TypeError):
        encrypt_message("Joey", "3")

    # Se key não for um índice válido, retorna a string message invertida

    message = "Joey"
    key = 7
    assert encrypt_message(message, key) == "yeoJ"

    # Se key for um índice valido e par

    message = "Joey"
    key = 2
    assert encrypt_message(message, key) == "ye_oJ"

    # Se key for um índice valido e ímpar

    message = "Joey"
    key = 3
    assert encrypt_message(message, key) == "eoJ_y"
