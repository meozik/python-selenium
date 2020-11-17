from selenium import webdriver
import time
import math

URL="http://suninjuly.github.io/cats.html"

browser = webdriver.Chrome()
browser.get(URL)

browser.find_element_by_id("button")