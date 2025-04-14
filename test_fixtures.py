import pytest


@pytest.fixture
def login_page(open_browser):
    print("Login page opened!")
    pass

@pytest.fixture
def user():
    print("Username and password entered!")
    return "username", "password"

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


