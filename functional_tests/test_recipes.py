import re

import pytest
from django.core import mail
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

User = get_user_model()


def wait_for_element(driver, element_id, wait_time=2):
    """Wait for an element with given id to show up on the page."""
    WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[@id='{element_id}']"))
    )


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()


@pytest.mark.django_db
def test_sign_up_and_first_recipe(live_server, driver):
    # User tom exists
    email = "tom@example.com"
    User.objects.create_superuser("tom", email)

    # Tom navigates to the homepage and see's "Tom's Website" as the title
    driver.get(live_server.url)
    assert "Tom's Website" in driver.title, "title not found"

    # Tom clicks on the recipes link
    driver.find_element(By.LINK_TEXT, "Recipes").click()

    # Tom clicks on the link to add a new recipe
    driver.find_element(By.LINK_TEXT, "Add New Recipe").click()

    # Tom is first asked to log in
    elem = driver.find_element(By.NAME, "email")
    elem.send_keys(email)
    elem.send_keys(Keys.RETURN)
    wait_for_element(driver, "message")
    body = mail.outbox[0].body
    link = re.search(r"http:\/\/localhost:[\w\/?=]+", body).group()
    # TODO use a retry instead?
    import time

    time.sleep(5)
    driver.get(link)

    # Tom goes back to the page to add a new recipe
    driver.find_element(By.LINK_TEXT, "Recipes").click()
    driver.find_element(By.LINK_TEXT, "Add New Recipe").click()

    # Tom adds a recipe URL
    url = "https://example.com/recipe"
    elem = driver.find_element(By.NAME, "url")
    elem.send_keys(url)

    # Tom adds a title
    title = "my recipe"
    elem = driver.find_element(By.NAME, "title")
    elem.send_keys(title)

    # Tom adds notes
    notes = "some notes about this recipe"
    elem = driver.find_element(By.NAME, "notes")
    elem.send_keys(notes)

    driver.find_element(By.NAME, "submit").click()

    # Top is redirected to the recipes page
    # TODO use the wait_for
    time.sleep(2)
    assert driver.current_url.endswith("/recipes/")

    # Tom then sees the recipe listed
    elem = driver.find_element(By.LINK_TEXT, title)

    # The link points to the recipe's url
    assert url == elem.get_attribute("href")

    # Tom also sees the recipe's notes
    assert driver.find_element(By.NAME, "notes").text == notes

    # Tom can edit the the recipe
    driver.find_element(By.LINK_TEXT, "Edit").click()

    # Tom changes the title
    title = "my modified recipe"
    elem = driver.find_element(By.NAME, "title")
    elem.clear()
    elem.send_keys(title)

    # Tom changes notes
    notes = "some other notes about this recipe"
    elem = driver.find_element(By.NAME, "notes")
    elem.clear()
    elem.send_keys(notes)

    # Tom changes the url
    url = "https://example.com/recipe_modified"
    elem = driver.find_element(By.NAME, "url")
    elem.clear()
    elem.send_keys(url)

    driver.find_element(By.NAME, "submit").click()

    # Tom sees the updates
    elem = driver.find_element(By.LINK_TEXT, "Link")
    assert url == elem.get_attribute("href")
    elem = driver.find_element(By.NAME, "notes")
    assert notes == elem.text
    elem = driver.find_element(By.NAME, "title")
    assert title == elem.text

    # Tom can delete the recipe
    driver.find_element(By.LINK_TEXT, "Delete").click()
    driver.find_element(By.NAME, "submit").click()

    # Tom is back on the list page
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Add New Recipe")
