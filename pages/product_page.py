from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    """" Класс описания страницы товара """
    def add_product_in_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON_ADD_IN_BASKET)
        button_add_basket.click()
        self.solve_quiz_and_get_code()

    def name_book_the_same(self):
        name_book_add = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_IN_BASKET).text
        name_book_added = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_IN_BASKET).text
        assert name_book_add == name_book_added, "Book is not verify"
