# coding=utf-8
"""
Created on 2019-05-05
@author: Four
Project: operation-活动
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
from Utils.Selection_Menu import Fixed_Window, is_frame_page, Selection_Menu
from Utils.DriverWait import Wait_Click, Send_Key, Send_Picture, page_Refresh, page_scrolling, public_time, select_list
logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间


class Operation_Activity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def add_activity(self, name, image, activity_type, piece, money, apply_product, together, product_name):
        u"""添加活动"""
        try:
            Wait_Click(self.browser, Activity().add_activity)
            Send_Key(self.browser, Activity().promotion_subject, name)  # 促销主题
            Send_Key(self.browser, Activity().promotion_time, public_time(days=2))  # 促销时间
            Send_Picture(self.browser, Activity().promotion_photo, Add_product_information_path().carousel_product % format(image))  # 促销首图
            Wait_Click(self.browser, Activity().activity_type % format(activity_type))  # 促销规则
            if activity_type == 1:  # 满减活动
                Wait_Click(self.browser, Activity().type_piece)
                Send_Key(self.browser, Activity().type_piece, piece)
                Wait_Click(self.browser, Activity().type_money)
                Send_Key(self.browser, Activity().type_money, money)
            elif activity_type == 2:    # 满折活动
                Wait_Click(self.browser, Activity().type_piece)
                Send_Key(self.browser, Activity().type_piece, piece)
                Wait_Click(self.browser, Activity().type_money)
                Send_Key(self.browser, Activity().type_money, money)
            Wait_Click(self.browser, Activity().apply_product % format(apply_product))  # 适用商品：1.全部 2.指定
            if apply_product == 1:
                pass
            elif apply_product == 2:
                Wait_Click(self.browser, Activity().add_product)
                Send_Key(self.browser, Activity().query_product_name, product_name)
                Wait_Click(self.browser, Activity().query_product_name_button)
                Wait_Click(self.browser, Activity().select_product % format(2))
                Wait_Click(self.browser, Activity().product_ensure)
            Wait_Click(self.browser, Activity().discount_coupon_together % format(together))  # 是否能与优惠券：1.是 2.否
            page_scrolling(self, scroll=1)  # 下滚
            Wait_Click(self.browser, Activity().activity_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def query_activity(self, name):
        try:
            Wait_Click(self.browser, Activity().query_activity_status)
            select_list(self, name=name, get_list=Activity().query_activity_status_list)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    @unittest.skip('无条件跳过')
    def test_add_Activity(self):
        u"""添加活动"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Production_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Production_Management_path().Activity)
        is_frame_page(self, Production_Management_frame().Activity_frame)
        self.add_activity(name='活动主题', image=10, activity_type=1, piece=1,
                          money=1, apply_product=2, together=1, product_name='西门子')

    # @unittest.skip('无条件跳过')
    def test_query_Activity(self):
        u"""查询活动"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Production_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Production_Management_path().Activity)
        is_frame_page(self, Production_Management_frame().Activity_frame)
        self.query_activity(name='未开始')

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
