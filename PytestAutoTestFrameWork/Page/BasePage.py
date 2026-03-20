import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from util.clipboard import ClipBoard
from util.keyboard import KeyBoard
from util.parseConFile import ParseConFile
from util.parseExcelFile import ParseExcel

class BasePage:
    cf = ParseConFile()
    excel = ParseExcel()

    def __init__(self, driver, outTime=30):
        self.driver = driver
        self.outTime = outTime
        self.byDic = {
            'id': By.ID, 'name': By.NAME,
            'class_name': By.CLASS_NAME, 'xpath': By.XPATH
        }

    def findElement(self, by, locator):
        return WebDriverWait(self.driver, self.outTime).until(
            lambda x: x.find_element(self.byDic[by], locator)
        )

    def click(self, by, locator):
        element = WebDriverWait(self.driver, self.outTime).until(
            EC.element_to_be_clickable((self.byDic[by], locator))
        )
        element.click()

    def sendKeys(self, by, locator, value):
        self.findElement(by, locator).send_keys(value)

    def switchToFrame(self, by, locator):
        WebDriverWait(self.driver, self.outTime).until(
            EC.frame_to_be_available_and_switch_to_it((self.byDic[by], locator))
        )

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def ctrlV(self, value):
        ClipBoard.setText(value)
        time.sleep(2)
        KeyBoard.twoKeys('ctrl', 'v')

    def enterKey(self):
        KeyBoard.oneKey('enter')

    def getElementText(self, by, locator):
        return self.findElement(by, locator).text

    def loadUrl(self, url):
        self.driver.get(url)