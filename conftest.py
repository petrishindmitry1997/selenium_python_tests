import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # choose browser (chrome default)
	parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: firefox or chrome")
    # choose lang
	parser.addoption('--language', action='store', default=None, help="Say language name to select")

@pytest.fixture(scope="function")
def browser(request):

	# choose language
    choosen_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
		# chrome init
        opts = Options()
        opts.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
        opts.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(options=opts)
    elif browser_name == "firefox":
	    # firefox init
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", choosen_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
