import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture
def setup(request):

    global driver
    browser = request.config.getoption("browser")

    if browser == "chrome":

        service1 = Service("G:\\PytestFramework\\testcases\\chromedriver.exe")
        driver = webdriver.Chrome(service=service1)

    elif browser == "edge":
        service = Service("G:\\PytestFramework\\testcases\\msedgedriver.exe")
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(service=service, options=options)

    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/account")
    request.cls.driver = driver
    yield
    driver.quit()