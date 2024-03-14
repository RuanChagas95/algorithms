from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    invalids = [("hello", None), (None, 3), (1, 1)]
    for invalid in invalids:
        with pytest.raises(Exception):
            encrypt_message(*invalid)
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("hello", 9) == "olleh"
    assert encrypt_message("hello", 4) == "o_lleh"
    assert encrypt_message("hello", -1) == "olleh"
