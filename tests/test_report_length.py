from lib.report_length import *

def test_length():
    assert report_length("Hello") == "This string was 5 characters long."
    assert report_length("And") == "This string was 3 characters long."
    assert report_length("What") == "This string was 4 characters long."
    assert report_length("hyrhfyhrydfhrhfesgflsgvelusgvfl") == "This string was 31 characters long."
    assert report_length("Antidusty") == "This string was 9 characters long."
