from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    """" Класс описания страницы товара """
    def add_product_in_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON_ADD_IN_BASKET)
        button_add_basket.click()

    def name_book_the_same(self):
        name_book_add = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_IN_BASKET).text
        name_book_added = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_IN_BASKET).text
        assert name_book_add == name_book_added, "Book is not verify"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_IN_BASKET), \
            "Success message is presented, but should be disappeared"
