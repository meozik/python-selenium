from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

URL = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    treasure = browser.find_element_by_id("treasure")
    valuex = treasure.get_attribute("valuex")
    browser.find_element_by_id("answer").send_keys(calc(valuex))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_css_selector("[value='robots']").click()
    browser.find_element_by_css_selector("[type='submit']").click()
finally:
    time.sleep(5)
    browser.quit()
