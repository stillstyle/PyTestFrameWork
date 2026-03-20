import pytest
from Page.PageObject.LoginPage import LoginPage

@pytest.mark.loginTest
class TestLogin:
    loginSheet = LoginPage.getSheet('login')
    data = LoginPage.excel.getAllValuesOfSheet(loginSheet)
    userName = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'username')
    passWord = LoginPage.cf.getLocatorsOrAccount('126LoginAccount', 'password')

    @pytest.fixture
    def teardown_func(self, driver):
        yield
        driver.delete_all_cookies()

    @pytest.mark.parametrize('username, password, expect', data)
    def test_login(self, teardown_func, driver, username, password, expect):
        login = LoginPage(driver, 30)
        login.login(username, password)
        login.sleep(5)
        if username == self.userName and password == self.passWord:
            login.assertValueInSource(expect)
        else:
            login.assertTextEqString(expect)