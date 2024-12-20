from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "[value='Add to basket']")
    HEADER_OF_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    FIRST_MESSAGE_ABOUT_ADDING_TO_THE_BASKET = (By.CSS_SELECTOR, "#messages div.alert:first-child")
    THIRD_MESSAGE_ABOUT_ADDING_TO_THE_BASKET = (By.CSS_SELECTOR, "#messages div.alert:last-child")
