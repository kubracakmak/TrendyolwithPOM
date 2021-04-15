import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from static.commonOperations import commonOperations
from static import info

class Test_login():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    driver = webdriver.Chrome(chrome_options=option, executable_path=info.driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(info.url)

    comOpr = commonOperations(driver)

    def test_1(self):
        test = Test_login()
        test.comOpr.enterUsername(info.username)
        test.comOpr.enterPassword(info.password)
        test.comOpr.clickLogin()
        time.sleep(15)