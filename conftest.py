import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # choose language
    parser.addoption('--language', action='store', default='ru',
                     help="Выберите предпочтительный язык сайта, например: fr")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    print("\nChrome launch {}".format(user_language))
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # chrome init
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
