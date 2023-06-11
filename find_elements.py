import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByID:
    def locate_by_id(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        list = driver.find_elements(By.TAG_NAME, 'a')
        print(len(list))
        for i in list:
            print(i.text)
        time.sleep(4)

find_by_id = DemoFindElementByID()
find_by_id.locate_by_id()
