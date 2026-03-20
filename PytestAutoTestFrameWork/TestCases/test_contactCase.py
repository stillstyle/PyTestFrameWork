import re
import pytest
from Page.PageObject.HomePage import HomePage
from Page.PageObject.ContactPage import ContactPage

@pytest.mark.contactTest
class TestAddContact:
    contactSheet = ContactPage.getSheet('contact')
    data = ContactPage.excel.getAllValuesOfSheet(contactSheet)

    @pytest.mark.parametrize('Name, Mail, Star, Phone, Comment, expect', data)
    def test_NewContact(self, driver, login, Name, Mail, Star, Phone, Comment, expect):
        home = HomePage(driver)
        contact = ContactPage(driver)
        home.selectMenu()
        contact.newContact(Name, Mail, Star, Phone, Comment)
        if re.match(r'^.{1,}@[0-9a-zA-Z]{1,13}\..*$', Mail):
            contact.assertValueInSource(expect)
        else:
            contact.assertErrorTip(expect)