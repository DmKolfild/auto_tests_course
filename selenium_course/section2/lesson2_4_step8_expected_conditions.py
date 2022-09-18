from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    # Открыть страницу
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    browser.implicitly_wait(12)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажать на кнопку "Book"
    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    # Решить математическую задачу и отправить решение
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    button_solve = browser.find_element(By.ID, "solve")
    button_solve.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

