import time
from static import info
from static import locators

class commonOperations():

    def __init__(self, driver):
        self.driver = driver
        self.usernameID = locators.Locators.usernameID
        self.passwordID = locators.Locators.passwordID
        self.loginButtonID = locators.Locators.loginButtonID


    def enterUsername(self, username):
        self.driver.find_element_by_id(self.usernameID).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.passwordID).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.loginButtonID).click()



