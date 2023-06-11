import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class GetAttributeValue:
    def get_value(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://training.openspan.com/login')
        attr_value = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(attr_value)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys('TestUser')
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys('TestUser345')
        attr_value = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(attr_value)
        time.sleep(4)


attr_obj = GetAttributeValue()
attr_obj.get_value()
