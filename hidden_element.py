import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class HiddenElement:
    def demo_is_displayed(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        element = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(element)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        element = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(element)
        time.sleep(4)

    def demo_is_displayed_yatra(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/hotels')
        driver.find_element(By.XPATH, "//i[@class='icon icon-angle-right arrowpassengerBox']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(2)
        age_drop = driver.find_element(By.XPATH, "//li[@class='col-x-fluid fl']//span[@class='pax-title']").is_displayed()
        print(age_drop)
        driver.find_element(By.XPATH, "(//span[@class='ddSpinnerMinus'])[2]").click()
        time.sleep(2)
        age_drop1 = driver.find_element(By.XPATH, "//li[@class='col-x-fluid fl']//span[@class='pax-title']").is_displayed()
        print(age_drop1)

# attr_obj = HiddenElement()
# attr_obj.demo_is_displayed()

displayed_or_hidden = HiddenElement()
displayed_or_hidden.demo_is_displayed_yatra()
