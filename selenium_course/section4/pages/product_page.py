from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_message_about_adding_in_basket(self):
        header_of_product = self.text_of_element(*ProductPageLocators.HEADER_OF_PRODUCT)
        first_message = self.text_of_element(*ProductPageLocators.FIRST_MESSAGE_ABOUT_ADDING_TO_THE_BASKET)
        price_of_product = self.text_of_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        third_message = self.text_of_element(*ProductPageLocators.THIRD_MESSAGE_ABOUT_ADDING_TO_THE_BASKET)
        assert (price_of_product in third_message
                and header_of_product in first_message), "Name of item is not presented in the basket's message"