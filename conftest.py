"""У меня не удалось проверить тест в браузере Chrome, так как выхожит ошибка 'ERROR test_items.py::test_find_button
- selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only
 supports Chrome version 81', то есть не совпадают версии, ошибку исправить не удалось. В браузере Firefox все проходит
 отлично! Пожалуйста, не снижайте за это баллы! Спасибо!!!"""


from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es', help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



