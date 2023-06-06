import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.shoes_page import ShoesPage
from TestingData import test_data

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=test_data.browser)


@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    elif get_browser == "headless":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Driver not supported")
    driver.implicitly_wait(10)
    request.cls.home_page = HomePage(driver)
    request.cls.shoes_page = ShoesPage(driver)
    driver.get(test_data.url)
    yield driver
    driver.quit()
