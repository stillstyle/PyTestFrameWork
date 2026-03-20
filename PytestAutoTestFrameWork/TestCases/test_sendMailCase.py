import pytest
from Page.PageObject.SendMailPage import SendMailPage

@pytest.mark.sendMailTest
class TestSendMail:
    sendMailSheet = SendMailPage.getSheet('mail')
    data = SendMailPage.excel.getAllValuesOfSheet(sendMailSheet)

    @pytest.mark.parametrize('Address, Subject, Text, PFA', data)
    def test_sendMail(self, driver, login, Address, Subject, Text, PFA):
        send_mail = SendMailPage(driver)
        send_mail.sendMail(Address, Subject, Text, PFA)
        assert send_mail.isElementExsit(*SendMailPage.expect)