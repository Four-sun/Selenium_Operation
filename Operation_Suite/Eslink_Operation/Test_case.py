# -*- coding: utf-8 -*-
"""
Created on 2019-01-07
@author: sun
Project:测试登陆ecc
"""

import time
import unittest

from selenium import webdriver

from Utils.Login_User import login_user


class EccTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(chrome_options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get("http://etbc-qa.eslink.net.cn/")

    def test_ecc_test(self):
        u"""ecc登陆"""

        login_user(self, u"0341zy", u"0341zy")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        print('执行完成!')

        cls.browser.quit()

if __name__ == '__main__':
    unittest.main()
