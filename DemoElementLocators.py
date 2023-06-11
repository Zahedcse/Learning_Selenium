import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByID:
    def locate_by_id(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(by='id', value='login-input').send_keys('Test@test.com')
        time.sleep(4)

find_by_id = DemoFindElementByID()
find_by_id.locate_by_id()
