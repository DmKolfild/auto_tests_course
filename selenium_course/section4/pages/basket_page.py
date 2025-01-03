from .base_page import BasePage
from .locators import BasketPageLocators

empty_message_in_different_languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en-gb": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def should_be_message_about_empty(self):
        actual_message_about_empty = self.get_text_of_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY)
        language = self.get_language_of_page()
        expected_message_about_empty = empty_message_in_different_languages[language]
        assert expected_message_about_empty in actual_message_about_empty, "Empty message is not presented, but should be"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FORM_WITH_ITEMS), \
            "Items is presented, but should not be"
