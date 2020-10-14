# coding=utf-8
"""
Created on 2019-04-30
@author: Four
Project: operation-首页标签
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
from Utils.DriverWait import Wait_Find, Wait_Click, Send_Key, Send_Picture, page_Refresh
logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间


class Home_Tag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def add_home_tag(self, name, sort, status, tag_type, image):
        u"""添加首页标签"""
        try:
            Wait_Click(self.browser, Home_Tag_Path().add_tag_button)
            Send_Key(self.browser, Home_Tag_Path().tag_name, name)
            Wait_Click(self.browser, Home_Tag_Path().tag_sort)
            Send_Key(self.browser, Home_Tag_Path().tag_sort, sort)
            Wait_Click(self.browser, Home_Tag_Path().tag_status)
            Wait_Click(self.browser, Home_Tag_Path().status % status)
            Wait_Click(self.browser, Home_Tag_Path().tag_type)
            Wait_Click(self.browser, Home_Tag_Path().type % tag_type)
            Send_Picture(self.browser, Home_Tag_Path().tag_photo, Add_product_information_path().carousel_product % format(image))
            Wait_Find(self.browser, (By.XPATH, Home_Tag_Path().update_photo))
            Wait_Click(self.browser, Home_Tag_Path().save_button)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def delete_home_tag(self, product):
        u"""删除标签"""
        try:
            Wait_Click(self.browser, Home_Tag_Path().choose_product % product)
            Wait_Click(self.browser, Home_Tag_Path().delete_button)
            Wait_Click(self.browser, Home_Tag_Path().delete_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def add_product(self, name, product):
        u"""添加商品"""
        try:
            Wait_Click(self.browser, Home_Tag_Path().add_product)
            Send_Key(self.browser, Home_Tag_Path().query_product_name, name)
            Wait_Click(self.browser, Home_Tag_Path().query_product_name_button)
            Wait_Click(self.browser, Home_Tag_Path().choose_product % product)
            Wait_Click(self.browser, Home_Tag_Path().add_product_button)
            Wait_Click(self.browser, Home_Tag_Path().get_back)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def delete_product(self, product):
        u"""删除商品"""
        try:
            Wait_Click(self.browser, Home_Tag_Path().choose_product % product)
            Wait_Click(self.browser, Home_Tag_Path().delete_product)
            Wait_Click(self.browser, Home_Tag_Path().delete_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def query_tag_name(self, name):
        u"""查询标签名称"""
        try:
            Send_Key(self.browser, Home_Tag_Path().query_tag_name, name)
            Wait_Click(self.browser, Home_Tag_Path().query_tag_name_button)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    @unittest.skip('无条件跳过')
    def test_add_Home_Tag(self):
        u"""添加首页标签"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Home_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Home_Management_path().Home_Tag)
        is_frame_page(self, Home_Management_frame().Home_Tag_frame)
        self.add_home_tag(name="自动标签", sort=2, status=1, tag_type=1, image=6)
        self.add_product(name='西门子', product=1)

    # @unittest.skip('无条件跳过')
    def test_query_Home_Tag(self):
        u"""首页标签查询"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Home_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Home_Management_path().Home_Tag)
        is_frame_page(self, Home_Management_frame().Home_Tag_frame)
        self.query_tag_name(name="自动标签")
        page_Refresh(self, Home_Tag_Path().close_menu)
        # self.delete_product(product=1)
        # self.delete_home_tag(product=1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
