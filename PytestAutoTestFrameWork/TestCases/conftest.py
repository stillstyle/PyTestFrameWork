import pytest
from Page.PageObject.LoginPage import LoginPage

userName = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'username')
passWord = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'password')

@pytest.fixture(scope='function')
def login(driver):
    loginFunc = LoginPage(driver, 30)
    loginFunc.login(userName, passWord)
    yield
    driver.delete_all_cookies()