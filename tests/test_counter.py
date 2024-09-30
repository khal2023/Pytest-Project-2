from lib.counter import *

def test_one():
    counter = Counter()
    counter.add(6)
    assert counter.report() == "Counted to 6 so far."

def test_two():
    counter2 = Counter()
    counter2.add(9)
    assert counter2.report() == "Counted to 9 so far."