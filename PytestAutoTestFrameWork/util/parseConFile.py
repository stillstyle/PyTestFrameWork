import configparser
from config.conf import configDir

class ParseConFile:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(configDir, encoding='utf-8')

    def getLocatorsOrAccount(self, section, option):
        locator = self.conf.get(section, option)
        if '->' in locator:
            return tuple(locator.split('->'))
        return locator