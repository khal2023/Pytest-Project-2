from lib.check_codeword import *

def test_check_one():
    codeword = check_codeword("horse")
    assert codeword == "Correct! Come in."

def test_check_two():
    assert check_codeword("hosre") == "Close, but nope."

def test_check_three():
    assert check_codeword("Khalid") == "WRONG!"