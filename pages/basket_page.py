from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_gods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_LINK), \
            "Goods is present, should not is present"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Massage 'Basket is empty' is not present"
