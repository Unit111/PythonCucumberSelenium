from contextlib import contextmanager

from aloe import around
from aloe import world
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@around.all
@contextmanager
def with_browser():

    world.browser = webdriver.Firefox(executable_path
                                      =r'C:\Users\Pesho\PycharmProjects\Cucumber\conf\geckodriver.exe')
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