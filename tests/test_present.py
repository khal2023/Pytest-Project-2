# Library importd
import pytest
from lib.present import *


def test_present():
    present = Present()
    present.wrap("Football")
    with pytest.raises(Exception) as e:
        present.wrap("Golf clubs")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_empty():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."

def test_full():
    present = Present()
    present.wrap("Football")
    assert present.unwrap() == "Football"
    