import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class DemoSelectorID:
    def selector_id(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://www.rokomari.com/login')
        driver.find_element(by='xpath', value="//input[@placeholder='Email or phone']").send_keys('Test@test.com')
        time.sleep(4)


Id_selector = DemoSelectorID()
Id_selector.selector_id()