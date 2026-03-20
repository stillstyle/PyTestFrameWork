import win32con
import win32clipboard as WC

class ClipBoard:
    @staticmethod
    def getText():
        WC.OpenClipboard()
        value = WC.GetClipboardData(win32con.CF_TEXT)
        WC.CloseClipboard()
        return value

    @staticmethod
    def setText(value):
        WC.OpenClipboard()
        WC.EmptyClipboard()
        WC.SetClipboardData(win32con.CF_UNICODETEXT, value)
        WC.CloseClipboard()