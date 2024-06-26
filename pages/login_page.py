from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Login link is not presented'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_AUTHORIZATION) \
               and self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_AUTHORIZATION) \
               and self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_SUBMIT), \
               "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_REGISTRATION) \
               and self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_REGISTRATION) \
               and self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_REGISTRATION), \
               "Register form is not presented"

    def register_new_user(self):
        message = str(time.time()) + "@fakemail.org"
        email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_REGISTRATION)
        email.send_keys(message)
        password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_REGISTRATION)
        password.send_keys(message)
        password_repeat = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_REGISTRATION_REPEAT)
        password_repeat.send_keys(message)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_REGISTRATION).click()
