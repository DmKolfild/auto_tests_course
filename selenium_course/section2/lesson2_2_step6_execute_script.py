from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    # Открыть страницу
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    #Посчитать математическую функцию от x
    x = x_element.text
    y = calc(x)

    # Проскроллить страницу вниз
    browser.execute_script("window.scrollBy(0, 150);")

    # Ввести ответ в текстовое пол
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # Выбрать checkbox "I'm the robot"
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    # Переключить radiobutton "Robots rule!"
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    # Нажать на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
