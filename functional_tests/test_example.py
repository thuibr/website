import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()


def test_title(live_server, driver):
    driver.get(live_server.url)
    assert "Tom's Website" in driver.title, "title not found"
