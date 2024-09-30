from lib.greet import *

def test_greeting():
    greeting = greet("John")
    assert greeting == "Hello, John!"