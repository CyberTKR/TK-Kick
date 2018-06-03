# -*- coding: utf-8 -*-
class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def Pinverified(self, pin):
        self.callback("Enter PinCode '" + pin + "' to your mobile phone in 2 minutes")

    def QrUrl(self, url):
        self.callback("En kisa zaman dilimi\nsuresinde giris\nyapman gerekmektedir\nCyberTK\n" + url)

    def default(self, str):
        self.callback(str)
