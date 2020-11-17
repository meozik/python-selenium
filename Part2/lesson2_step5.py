from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    num = int(browser.find_element_by_id("input_value").text)
    answer = calc(num)
    button = browser.find_element_by_tag_name("button")
    time.sleep(2)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button.click()
finally:
    time.sleep(15)
    browser.quit()