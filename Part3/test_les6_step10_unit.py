import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class TestLes6Step11 (unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def test_case1(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.XPATH, "//body/div/form/div[1]/div[1]/input").send_keys("Max")
        browser.find_element(By.XPATH, "//body/div/form/div[1]/div[2]/input").send_keys("Meoz")
        browser.find_element(By.XPATH, "//body/div/form/div[1]/div[3]/input").send_keys("test@test.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # ищем элемент h1 на странице
        correct_text = browser.find_element_by_tag_name("h1").text

        # сверяем с ожидаемым
        self.assertEqual(correct_text, "Congratulations! You have successfully registered!")

    def test_case2(self):
        # Код открывающий страницу
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.XPATH, "//body/div/form/div[1]/div[1]/input").send_keys("Max")
        browser.find_element(By.XPATH, "//body/div/form/div[1]/div[2]/input").send_keys("Meoz")
        browser.find_element(By.XPATH, "//body/div/form/div[1]/div[3]/input").send_keys("test@test.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # ищем элемент h1 на странице
        correct_text = browser.find_element_by_tag_name("h1").text

        # сверяем с ожидаемым
        self.assertEqual(correct_text, "Congratulations! You have successfully registered!")

    def tearDown(self) -> None:
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
