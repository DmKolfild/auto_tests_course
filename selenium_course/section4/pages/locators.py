from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, "[href*='/basket/']")
    HTML_WHOLE_PAGE = (By.XPATH, "//html")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "[value='Add to basket']")
    HEADER_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    FIRST_MESSAGE_ABOUT_ADDING_TO_THE_BASKET = (By.CSS_SELECTOR, "#messages div.alert:first-child strong")
    THIRD_MESSAGE_ABOUT_ADDING_TO_THE_BASKET = (By.CSS_SELECTOR, "#messages div.alert:last-child strong")


class BasketPageLocators:
    MESSAGE_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    FORM_WITH_ITEMS = (By.CSS_SELECTOR, "#basket_formset")
