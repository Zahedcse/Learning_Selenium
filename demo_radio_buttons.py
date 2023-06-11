import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoRadioButtons:
    def demo_radio_buttons(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        # time.sleep(5)
        driver.find_element(By.XPATH, "(//i[@class='ico ico-checkbox'])[2]").click()
        var1 = driver.find_element(By.NAME, "non_stop").is_selected()
        print(var1)
        # driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").click()
        # var2 = driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").is_selected()
        # print(var2)
        time.sleep(3)


checkboxes = DemoRadioButtons()
checkboxes.demo_radio_buttons()

