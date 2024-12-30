from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_message_about_adding_in_basket_with_name_of_item(self):
        header_of_product = self.get_text_of_element(*ProductPageLocators.HEADER_OF_PRODUCT)
        first_message = self.get_text_of_element(*ProductPageLocators.FIRST_MESSAGE_ABOUT_ADDING_TO_THE_BASKET)
        assert header_of_product == first_message, "Name of Item is not presented in the basket's message"

    def should_be_message_about_adding_in_basket_with_price_of_item(self):
        price_of_product = self.get_text_of_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        third_message = self.get_text_of_element(*ProductPageLocators.THIRD_MESSAGE_ABOUT_ADDING_TO_THE_BASKET)
        assert price_of_product == third_message, "Price of Item is not presented in the basket's message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
