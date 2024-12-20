from selenium.webdriver.common.by import By


# pytest --language=es .\test_lesson3_6_step10_language.py


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_supplys_contains_add_to_cart_button(browser):
    browser.implicitly_wait(10)
    browser.get(link)

    button = browser.find_elements(By.CSS_SELECTOR, "#id_quantity + button")

    assert button, "Button is not found!"
