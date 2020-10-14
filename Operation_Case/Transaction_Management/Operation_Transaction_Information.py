# coding=utf-8
"""
Created on 2019-04-10
@author: Four
Project: operation-交易信息
"""
import sys
import random
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
from Utils.DriverWait import Wait_Find, Wait_Click, Send_Key, Send_Picture, Wait_Text_present
logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间


class Transaction_Information(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def query_transaction_information(self, order_number='', mobile='', consignee='', order_time='', status=''):
        u"""
        查询交易信息
        状态列表1.待付款2.待发货3.待收货4.待评价5.退货/售后6.已关闭7.已完成
        """
        try:
            Send_Key(self.browser, Transaction_information_path().query_order_number, order_number)
            Send_Key(self.browser, Transaction_information_path().query_mobile, mobile)
            Send_Key(self.browser, Transaction_information_path().query_consignee, consignee)
            Send_Key(self.browser, Transaction_information_path().query_order_time, order_time)
            if status != '':
                Wait_Click(self.browser, Transaction_information_path().query_order_status)
                Wait_Click(self.browser, Transaction_information_path().status % status)
            else:
                pass
            Wait_Click(self.browser, Transaction_information_path().query_button)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def record_delivery(self, delivery='', site='', company='', postcode='', remark=''):
        u"""订单发货"""
        try:
            self.browser.implicitly_wait(5)
            Wait_Click(self.browser, Transaction_information_path().delivery_button % delivery)
            Wait_Click(self.browser, Transaction_information_path().record_delivery_button)
            Wait_Click(self.browser, Transaction_information_path().site)
            Wait_Click(self.browser, Transaction_information_path().site_list % site)
            Wait_Click(self.browser, Transaction_information_path().logistics_company)
            Wait_Click(self.browser, Transaction_information_path().logistics_company_list % company)
            Send_Key(self.browser, Transaction_information_path().logistics_number, random.randrange(1000000000,9999999999))
            Send_Key(self.browser, Transaction_information_path().postcode, postcode)
            Send_Key(self.browser, Transaction_information_path().remark, remark)
            Wait_Click(self.browser, Transaction_information_path().choose_all_product)
            Wait_Click(self.browser, Transaction_information_path().ensure_button)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def refund_audit(self):
        u"""订单退款审核"""
        try:
            Wait_Click(self.browser, Transaction_information_path().refund_audit % format(1))
            Wait_Text_present(self.browser, Transaction_information_path().refund_button, '审核')
            Wait_Click(self.browser, Transaction_information_path().refund_button)
            Wait_Click(self.browser, Transaction_information_path().refund_agree)
            Wait_Click(self.browser, Transaction_information_path().audit_ensure_button)    # 审核确定按钮
            Wait_Click(self.browser, Transaction_information_path().refund_button)
            Wait_Click(self.browser, Transaction_information_path().refund_ensure_button)   # 退款确定按钮
            Wait_Text_present(self.browser, Transaction_information_path().refund_button, '更新')
            Wait_Click(self.browser, Transaction_information_path().refund_button)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    # @unittest.skip('无条件跳过')
    def test_Transaction_Information(self):
        u"""交易信息"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Transaction_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Transaction_Management_path().Transaction_Information)
        is_frame_page(self, Transaction_Management_frame().Transaction_Information_frame)
        self.query_transaction_information(consignee='张阳', status='2')
        # self.record_delivery(delivery='1', site='1', company='1', postcode='311115', remark='测试自动发货')
        # self.refund_audit()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
