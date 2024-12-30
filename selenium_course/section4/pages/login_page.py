from multiprocessing.resource_tracker import register

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password_input2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        register_button.click()

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