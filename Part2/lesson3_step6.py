from selenium import webdriver
import time
import math

URL="http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    browser.find_element_by_tag_name("button").click()
    current_window = browser.current_window_handle
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()
