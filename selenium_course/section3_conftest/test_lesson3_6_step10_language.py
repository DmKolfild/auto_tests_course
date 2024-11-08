from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_supplys_contains_add_to_cart_button(browser):
    browser.implicitly_wait(10)
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "#id_quantity + button")

    assert button, "Button is not found!"
