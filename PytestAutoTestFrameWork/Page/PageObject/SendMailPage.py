from Page.BasePage import BasePage

class SendMailPage(BasePage):
    writeMail = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'writeMail')
    addressee = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'addressee')
    subject = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'subject')
    iframe = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'iframe')
    text = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'text')
    sendBtn = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'sendBtn')
    expect = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'expect')
    uploadAttachment = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'uploadAttachment')
    delete = BasePage.cf.getLocatorsOrAccount('SendMailPageElements', 'delete')

    def sendMail(self, Address, Subject, Text, PFA=''):
        self.click(*SendMailPage.writeMail)
        self.sendKeys(*SendMailPage.addressee, Address)
        self.sendKeys(*SendMailPage.subject, Subject)
        self.switchToFrame(*SendMailPage.iframe)
        self.sendKeys(*SendMailPage.text, Text)
        self.switchToDefaultFrame()
        if PFA:
            self.click(*SendMailPage.uploadAttachment)
            self.ctrlV(PFA)
            self.enterKey()
            self.waitElementtobelocated(*SendMailPage.delete)
        self.click(*SendMailPage.sendBtn)