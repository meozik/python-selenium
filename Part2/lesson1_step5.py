from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

site_url = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(site_url)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    answer = calc(x)
    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(answer)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobtn = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobtn.click()
    submit = browser.find_element_by_class_name("btn.btn-default")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
