from Page.BasePage import BasePage

class LoginPage(BasePage):
    frame = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'frame')
    username = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'username')
    password = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'password')
    loginBtn = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'loginBtn')
    ferrorHead = BasePage.cf.getLocatorsOrAccount('LoginPageElements', 'ferrorHead')

    def login(self, userName, passWord):
        self.loadUrl('https://mail.126.com')
        self.switchToFrame(*LoginPage.frame)
        self.sendKeys(*LoginPage.username, userName)
        self.sendKeys(*LoginPage.password, passWord)
        self.click(*LoginPage.loginBtn)
        self.switchToDefaultFrame()

    def assertTextEqString(self, expected):
        self.switchToFrame(*LoginPage.frame)
        text = self.getElementText(*LoginPage.ferrorHead)
        self.switchToDefaultFrame()
        assert text == expected