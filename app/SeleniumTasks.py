from contextlib import contextmanager

import os
from aloe import around
from aloe import world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@around.all
@contextmanager
def with_browser():
    driver_path = os.path.dirname(os.path.realpath(__file__)).replace("app", "conf\geckodriver.exe")
    world.browser = webdriver.Firefox(executable_path = driver_path)
    world.browser.maximize_window()
    yield
    world.browser.quit()
    delattr(world, 'browser')


def openGoogle():
    world.browser.get("http://google.com")


def searchFor(searchString):
    element = world.browser.find_element_by_css_selector('#lst-ib')
    element.send_keys(searchString, Keys.RETURN)


def openAbv():
    world.browser.get("http://abv.bg")