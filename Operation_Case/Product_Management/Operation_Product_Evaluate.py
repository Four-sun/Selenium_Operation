# coding=utf-8
"""
Created on 2019-04-08
@author: Four
Project: operation-商品评价
"""
import sys
import time
import unittest
from Utils.log import Logger
from selenium import webdriver
from Constant.Constant_Path import *
from Constant.Page_element_path import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utils.Login_User import login_user, Operation_Center
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from Utils.Selection_Menu import Fixed_Window, is_frame_page, Selection_Menu
from Utils.DriverWait import Wait_Click, Send_Key, Calculate_inventory, Wait_Text_present
logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间


class Product_Evaluate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def check_product_evaluate(self):
        u"""商品评价审核"""
        try:
            Wait_Click(self.browser, Product_evaluate_path().choose_product % format(1))
            Wait_Click(self.browser, Product_evaluate_path().visible % format(1))
            Send_Key(self.browser, Product_evaluate_path().response, '商品自动评价')
            Wait_Click(self.browser, Product_evaluate_path().ensure_button)
            Wait_Text_present(self.browser, Product_evaluate_path().prompt_message, "审核成功")
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_product_evaluate(self):
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Product_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Product_Management_path().Product_Evaluate)
        is_frame_page(self, Product_Management_frame().Product_Evaluate_frame)
        self.check_product_evaluate()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
