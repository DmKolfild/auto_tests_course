from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    # Открыть страницу
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    x_element = browser.find_element(By.ID, "treasure")
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x = x_element.get_attribute("valuex")
    print(type(x))
    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Отметить checkbox "I'm the robot"
    option_checkbox = browser.find_element(By.ID, "robotCheckbox")
    option_checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    option_radiobutton = browser.find_element(By.ID, "robotsRule")
    option_radiobutton.click()

    # Нажать на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()