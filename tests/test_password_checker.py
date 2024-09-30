import pytest
from lib.password_checker import*

def test_valid_password():
    password = PasswordChecker()
    assert password.check("Cooolibaly") == True
    assert password.check("jjjjjjjjjjjjjjjjjj") == True
    assert password.check("hvgdzsivgopsanga") == True


def test_invalid_password():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("hello")
    error_check = str(e.value) 
    assert error_check == "Invalid password, must be 8+ characters."


    