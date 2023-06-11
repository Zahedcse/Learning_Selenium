import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoDropDownMulti:
    def demo_drop_down_multi(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demoqa.com/select-menu")
        dd_demo = driver.find_element(By.ID, 'cars')
        dd_multiple = Select(dd_demo)

        dd_multiple.select_by_index(0)
        time.sleep(2)
        dd_multiple.select_by_value('saab')
        time.sleep(2)
        dd_multiple.select_by_visible_text('Opel')
        time.sleep(2)
        dd_multiple.select_by_index(3)
        time.sleep(2)
        dd_multiple.deselect_by_index(2)
        time.sleep(2)
        dd_multiple.deselect_by_value('saab')
        time.sleep(2)
        dd_multiple.deselect_all()

dddemo = DemoDropDownMulti()
dddemo.demo_drop_down_multi()


