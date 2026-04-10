import pytest
from utils.drivers import get_chrome_driver

@pytest.fixture()
def driver():
    browser = get_chrome_driver()
    yield browser
    browser.quit()