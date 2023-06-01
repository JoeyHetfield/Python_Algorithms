from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "Joey"
    key = 3
    assert encrypt_message(message, key) ==  "eJyo_"

