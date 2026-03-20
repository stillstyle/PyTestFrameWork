import win32api
import win32con
import time

class KeyBoard:
    vk_code = {
        'enter': 0x0D, 'tab': 0x09,
        'ctrl': 0x11, 'v': 0x56, 'a': 0x41, 'x': 0x58
    }

    @staticmethod
    def keyDown(key_name):
        win32api.keybd_event(KeyBoard.vk_code[key_name], 0, 0, 0)

    @staticmethod
    def keyUp(key_name):
        win32api.keybd_event(KeyBoard.vk_code[key_name], 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def twoKeys(key1, key2):
        KeyBoard.keyDown(key1)
        KeyBoard.keyDown(key2)
        KeyBoard.keyUp(key1)
        KeyBoard.keyUp(key2)