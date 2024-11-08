import time
from selenium.webdriver.common.by import By


# pytest -s -v --browser_name=chrome test_parser_example3_6_step6_fixture_request.py
# pytest -s -v --browser_name=firefox test_parser_example3_6_step6_fixture_request.py

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
