import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()


def test_sign_up_and_first_recipe(live_server, driver):

    # Tom navigates to the homepage and see's "Tom's Website" as the title
    driver.get(live_server.url)
    assert "Tom's Website" in driver.title, "title not found"

    # Tom also sees a Sign Up link
    driver.find_element(By.LINK_TEXT, 'Sign Up').click()

    # Tom clicks the link and is taken to the Sign Up page
    assert "Sign Up" in driver.title, "title not found"

    # Tom signs up with email tom@example.com and no password
    elem = driver.find_element(By.NAME, 'email')
    elem.send_keys("tom@example.com")
    elem.send_keys(Keys.RETURN)

    # Tom receives an email in his inbox to login

    # Tom logs in via the link in the email

    # Tom sees a link to the recipes section of the website

    # Tom clicks on it

    # Tom sees a link to add a new recipe

    # Tom adds a recipe URL

    # Tom then sees the recipe's title in a list on the recipes website

    pytest.fail("Finish the test!")
