import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose chrome or firefox')
    parser.addoption('--language', action='store', default='en', help='Choose ru or en')


# Фикстура для запуска в зависимости от выбранного браузера и языка
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == 'chrome':
        print("\n==================== START CHROME BROWSER FOR TEST.. ====================")
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print("\n==================== START FIREFOX BROWSER FOR TEST.. ====================")
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    yield browser
    print("\n==================== QUIT BROWSER.. ====================")
    browser.quit()
