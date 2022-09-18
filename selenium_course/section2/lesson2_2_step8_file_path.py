from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    # Открыть страницу
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Name")
    input_surname = browser.find_element(By.NAME, "lastname")
    input_surname.send_keys("Surname")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("Email")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    curren_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curren_dir, 'lesson2_2_step8_file_path.txt')
    input_file = browser.find_element(By.ID, "file")
    input_file.send_keys(file_path)

    # Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

