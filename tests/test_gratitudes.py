from lib.gratitudes import *

def test_gratitudes():
    thanks = Gratitudes()
    thanks.add("Dance!")
    thanks.add("song")
    assert thanks.format() == "Be grateful for: Dance!, song"


def test_thanks():
    thanks = Gratitudes()
    thanks.add("Hello")
    thanks.add("Beautiful")
    assert thanks.format() == "Be grateful for: Hello, Beautiful"

    
