from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

URL = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    answer = int(num1) + int(num2)
    print(answer)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(answer))
    browser.find_element_by_css_selector("[type='submit']").click()
finally:
    time.sleep(5)
    browser.quit()
