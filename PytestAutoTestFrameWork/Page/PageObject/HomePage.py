from Page.BasePage import BasePage

class HomePage(BasePage):
    mailList = BasePage.cf.getLocatorsOrAccount('HomePageElements', 'mailList')

    def selectMenu(self):
        self.click(*HomePage.mailList)