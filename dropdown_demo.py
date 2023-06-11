import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoDropDown:
    def demo_drop_down(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element(By.NAME, 'UserTitle')
        dd = Select(dropdown)
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_visible_text('Marketing / PR Manager')
        time.sleep(3)
        dd.select_by_value('CxO_General_Manager_AP')


dddemo = DemoDropDown()
dddemo.demo_drop_down()


