from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_EMAIL_AUTHORIZATION = (By.ID, 'id_login-username')
    LOGIN_PASSWORD_AUTHORIZATION = (By.ID, 'id_login-password')
    LOGIN_BUTTON_SUBMIT = (By.NAME, 'login_submit')

    LOGIN_EMAIL_REGISTRATION = (By.ID, 'id_registration-email')
    LOGIN_PASSWORD_REGISTRATION = (By.ID, 'id_registration-password1')
    LOGIN_PASSWORD_REGISTRATION_REPEAT = (By.ID, 'id_registration-password2')
    LOGIN_BUTTON_REGISTRATION = (By.NAME, 'registration_submit')