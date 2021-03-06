import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.fixture(scope="class")
# def browser():
#     browser = webdriver.Chrome()
#     browser.maximize_window()
#     browser.implicitly_wait(2)
#     yield browser
#     browser.quit()