from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from Part2.stepic_math import calc


try:
    URL = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(URL)

    print(browser.find_element_by_class_name("card-img-top").get_attribute("alt"))
    if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100")) is True:
        browser.find_element_by_id("book").click()
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_id("solve").click()
finally:
    time.sleep(15)
    browser.quit()