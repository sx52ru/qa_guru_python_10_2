
import pytest


@pytest.fixture(scope="session")
def open_browser():
    print("Browser opened!")

    yield

    print("Browser closed!")