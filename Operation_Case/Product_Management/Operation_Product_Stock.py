# coding=utf-8
"""
Created on 2019-04-07
@author: Four
Project: operation-商品库存
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
from Utils.DriverWait import Wait_Click, Send_Key, Calculate_inventory
logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间


class Product_Stock(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def in_product_stock(self):
        u"""商品入库"""
        Wait_Click(self.browser, Product_stock_path().choose_product % 1)
        Wait_Click(self.browser, Product_stock_path().in_and_out_management)
        Wait_Click(self.browser, Product_stock_path().in_storage)
        Send_Key(self.browser, Product_stock_path().in_and_out_number, 1)
        Send_Key(self.browser, Product_stock_path().in_and_out_remark, "商品入库")
        Wait_Click(self.browser, Product_stock_path().in_and_out_ensure_button)
        Calculate_inventory(self.browser, 0, Product_stock_path().Last_inventory,
                            Product_stock_path().This_inventory, Product_stock_path().in_and_out_inventory)

    def out_product_stock(self):
        u"""商品出库"""
        Wait_Click(self.browser, Product_stock_path().choose_product % 1)
        Wait_Click(self.browser, Product_stock_path().in_and_out_management)
        Wait_Click(self.browser, Product_stock_path().out_storage)
        Send_Key(self.browser, Product_stock_path().in_and_out_number, 1)
        Send_Key(self.browser, Product_stock_path().in_and_out_remark, "商品出库")
        Wait_Click(self.browser, Product_stock_path().in_and_out_ensure_button)
        Calculate_inventory(self.browser, 1, Product_stock_path().Last_inventory,
                            Product_stock_path().This_inventory, Product_stock_path().in_and_out_inventory)

    def query_product_stock(self):
        u"""查询商品库存"""
        try:
            Wait_Click(self.browser, Product_stock_path().query_product_classify)
            Wait_Click(self.browser, Product_stock_path().query_product_classify_list)
            Wait_Click(self.browser, Product_stock_path().query_product_classify_value)
            Send_Key(self.browser, Product_stock_path().query_product_name, '小米')
            Wait_Click(self.browser, Product_stock_path().query_button)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_product_stock(self):
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Product_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Product_Management_path().Product_Stock)
        is_frame_page(self, Product_Management_frame().Product_Stock_frame)
        self.query_product_stock()
        # self.in_product_stock()
        # self.out_product_stock()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
