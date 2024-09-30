from lib.string_builder import *

def test_one():
    string = StringBuilder()
    string.add("Hello")
    assert string.size() == 5
    assert string.output() == "Hello"


def test_two():
    string = StringBuilder()
    string.add("Go to hell!")
    assert string.size() == 11
    assert string.output() == "Go to hell!"