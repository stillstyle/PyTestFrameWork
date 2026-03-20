from Page.BasePage import BasePage

class ContactPage(BasePage):
    new_contact = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'new_contact')
    name = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'name')
    mail = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'mail')
    star = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'star')
    phone = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'phone')
    comment = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'comment')
    commit = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'commit')
    errortip = BasePage.cf.getLocatorsOrAccount('ContactPageElements', 'tooltip')

    def newContact(self, Name, Mail, Star, Phone, Comment):
        self.click(*ContactPage.new_contact)
        self.sendKeys(*ContactPage.name, Name)
        self.sendKeys(*ContactPage.mail, Mail)
        if Star == '1':
            self.click(*ContactPage.star)
        self.sendKeys(*ContactPage.phone, Phone)
        self.sendKeys(*ContactPage.comment, Comment)
        self.click(*ContactPage.commit)

    def assertErrorTip(self, excepted):
        text = self.getElementText(*ContactPage.errortip)
        assert text == excepted