# import pytest
from WeirdText import *
import os
example_texts = "example_texts"


def test_Constants_index():
    assert -1 == constants_index("Graal")
    assert 0 == constants_index(" Lancelot")
    assert 4 == constants_index("king\nArtur")
    assert 5 == constants_index("Parsi{}val")
    assert 15 == constants_index("HolyHandGrenade ")

def test_Shuffle_world():
    world = "Parrot"
    world2 = "Parr"
    for i in range(10000):
        assert world != shuffle_word(world)
        assert world2 != shuffle_word(world2)

def test_To_code():
    assert to_code("Wenn")
    assert ~to_code("ist")
    assert ~to_code("das")
    assert to_code("Nunstuck")
    assert ~to_code("git")
    assert ~to_code("und")
    assert to_code("slotermeyer")
    assert ~to_code("Ja")
    assert to_code("beiherhund")
    assert ~to_code("das")
    assert to_code("Oder")
    assert ~to_code("Die")
    assert to_code("Flipperwald")
    assert to_code("gerstuck")

def test_Decode_and_encode():
    texts = os.listdir(example_texts)
    for file_text in texts:
        if file_text.count("Test") != 1 or file_text.index("Test") != 0:
            continue
        with open(os.sep.join([example_texts, file_text]), "r") as f:
            text = f.read()
        assert text == decode(encode(text))        


