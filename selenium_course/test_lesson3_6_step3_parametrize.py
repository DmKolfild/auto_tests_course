import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link_list = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]

lost_message = ""

def calc():
    return math.log(int(time.time()))

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(f"\n\n\n{lost_message}\n\n\n")

@pytest.mark.parametrize('link', link_list)
def test_guest_should_see_correct_answer(browser, link):
    global lost_message
    browser.implicitly_wait(10)
    # открыть страницу
    browser.get(link)
    textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
    # ввести правильный ответ
    answer = calc()
    textarea.send_keys(answer)
    # нажать кнопку "Отправить"
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    button.click()
    # дождаться фидбека о том, что ответ правильный
    message = browser.find_element(By.CSS_SELECTOR, ".attempt__message > div > p")
    message = message.text
    if message != "Correct!":
        lost_message += message
    assert message == "Correct!", "Incorrect answer"
