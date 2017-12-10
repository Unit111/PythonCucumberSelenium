from aloe import world
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.remote_connection import LOGGER

from app.driver_provider import with_firefox
from app.selectors import *

webDriverWaitInSeconds = 5

def go_to_index():
    user_name = "demo@geri.life"
    password = "demo123"

    world.browser.get(geri_life_url)

    #TODO wait for page to load
    try:
        world.browser.find_element_by_css_selector("ul.nav:nth-child(1) > li:nth-child(1) > a:nth-child(1)")
    except NoSuchElementException:
        __find_element(username_field).send_keys(user_name)
        __find_element(password_field).send_keys(password)
        __find_element(login_button).click()

    __find_element("ul.nav:nth-child(1) > li:nth-child(1) > a:nth-child(1)")

def get_language():
    select_element = Select(__find_element(language_dropdown))
    return select_element.first_selected_option.text

def change_language(desired_language):
    select_element = Select(__find_element(language_dropdown))
    select_element.select_by_visible_text(desired_language)

def logout():
    __find_element(logout_button).click()


def __find_elements(selector):
    return world.browser.find_elements_by_css_selector(selector)


def __find_element(selector):
    element = WebDriverWait(world.browser, webDriverWaitInSeconds).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector)));
    return element


def __wait_for_page(url):
    wait = WebDriverWait(world.browser, webDriverWaitInSeconds)
    wait.until(EC.url_contains(url))
