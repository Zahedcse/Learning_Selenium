import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

class DemoAutoSuggestion:
    def demo_auto_suggestion(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://yatra.com/")
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys('New Delhi')
        time.sleep(3)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(5)
        going_to = driver.find_elements(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))



Suggestion = DemoAutoSuggestion()
Suggestion.demo_auto_suggestion()



