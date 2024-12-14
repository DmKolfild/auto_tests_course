from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_page_url = self.browser.current_url
        assert "login" in login_page_url

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
                & self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)), "Login form is not presented"

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
                & self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1)
                & self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1)), "Register form is not presented"