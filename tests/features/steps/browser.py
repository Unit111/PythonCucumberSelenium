from aloe import step

from app.SeleniumTasks import *

@step(r'the user opens google')
def openGoogleStep(self):
    with_browser()
    openGoogle()


@step(r"user searches for \"(.*?)\"")
def userSearchFor(self, searchString):
    searchFor(searchString)


@step(r'then opens abv')
def openGoogleStep(self):
    openAbv()