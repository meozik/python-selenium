from selenium import webdriver
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Max")
    browser.find_element_by_name("lastname").send_keys("Meoz")
    browser.find_element_by_name("email").send_keys("Test@test.com")
    # file_path = pathlib.PureWindowsPath("D:\Stepic_python+selenium\Part2\test.txt")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    # file_path = "D:\Stepic_python+selenium\Part2\fest.txt"
    print(file_path)
    browser.find_element_by_id("file").send_keys(str(file_path))
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()
