# coding=utf-8
"""
Created on 2019-04-12
@author: Four
Project: operation-首页大小轮播&首页菜单&首页公告
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
from Utils.DriverWait import Wait_Find, Wait_Click, Send_Key, Send_Picture, page_Refresh
logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间


class Home_Big_Wheel_Sow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def add_explain(self, title, address, image, rank, explain):
        u"""
        添加外部链接
        """
        try:
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_button)
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().add_title, title)   # 轮播标题
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().external_links)  # 外部链接
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().external_links_address, address)    # 外部链接地址
            Send_Picture(self.browser, Home_Big_Wheel_Sow_path().show_picture, Add_product_information_path().carousel_product % format(image))  # 展示图片
            Wait_Find(self.browser, (By.XPATH, Home_Big_Wheel_Sow_path().Prompt_Message))   # 等待图片上传完成
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().rank, rank)     # 排序
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().explain, explain)   # 说明
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().status)  # 状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().start_status)    # 启用状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def add_internal_activity(self, title, image, rank, explain,):
        u"""
        添加内部链接（活动详情）
        """
        try:
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_button)
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().add_title, title)  # 轮播标题
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().internal_links)  # 内部链接
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().internal_links_activity)  # 活动详情
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().choose_activity_button)   # 选择活动按钮
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().choose_activity_first)    # 选择第一个活动
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().choose_activity_ensure)
            Send_Picture(self.browser, Home_Big_Wheel_Sow_path().show_picture, Add_product_information_path().carousel_product % format(image))  # 展示图片
            Wait_Find(self.browser, (By.XPATH, Home_Big_Wheel_Sow_path().Prompt_Message))   # 等待图片上传完成
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().rank, rank)     # 排序
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().explain, explain)   # 说明
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().status)  # 状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().start_status)    # 启用状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def add_internal_product_list(self, title, one_level, two_level, image, rank, explain,):
        u"""
        添加内部链接（商品列表）
        """
        try:
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_button)
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().add_title, title)  # 轮播标题
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().internal_links)  # 内部链接
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().internal_links_product_list)  # 内部链接-商品列表
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().links_product_list)  # 商品列表
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().one_level_product % format(one_level))   # 一级分类
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().two_level_product % format(two_level))   # 二级分类
            Send_Picture(self.browser, Home_Big_Wheel_Sow_path().show_picture, Add_product_information_path().carousel_product % format(image))  # 展示图片
            Wait_Find(self.browser, (By.XPATH, Home_Big_Wheel_Sow_path().Prompt_Message))   # 等待图片上传完成
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().rank, rank)     # 排序
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().explain, explain)   # 说明
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().status)  # 状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().start_status)    # 启用状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def add_internal_product_details(self, title, product, image, rank, explain,):
        u"""
        添加内部链接（商品详情）
        """
        try:
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_button)
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().add_title, title)  # 轮播标题
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().internal_links)  # 内部链接
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().internal_links_product_details)  # 内部链接-商品详情
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().links_product_details)       # 选择商品
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().choose_product % format(product))  # 选择第一个商品
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().choose_product_ensure)
            Send_Picture(self.browser, Home_Big_Wheel_Sow_path().show_picture, Add_product_information_path().carousel_product % format(image))  # 展示图片
            Wait_Find(self.browser, (By.XPATH, Home_Big_Wheel_Sow_path().Prompt_Message))   # 等待图片上传完成
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().rank, rank)     # 排序
            Send_Key(self.browser, Home_Big_Wheel_Sow_path().explain, explain)   # 说明
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().status)  # 状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().start_status)    # 启用状态
            Wait_Click(self.browser, Home_Big_Wheel_Sow_path().add_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def delete_Home_Big_Wheel_Sow(self, is_all=None):
        u"""删除"""
        try:
            if is_all != None:
                Wait_Click(self.browser, Home_Big_Wheel_Sow_path().select_list % format(is_all))
                Wait_Click(self.browser, Home_Big_Wheel_Sow_path().delete_button)
                Wait_Click(self.browser, Home_Big_Wheel_Sow_path().delete_ensure)
            else:
                Wait_Click(self.browser, Home_Big_Wheel_Sow_path().select_all)
                Wait_Click(self.browser, Home_Big_Wheel_Sow_path().delete_button)
                Wait_Click(self.browser, Home_Big_Wheel_Sow_path().delete_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    # @unittest.skip('无条件跳过')
    def test_add_Home_Big_Wheel_Sow(self):
        u"""添加首页轮播（大）"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Home_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Home_Management_path().Home_Big_Wheel_Sow)
        is_frame_page(self, Home_Management_frame().Home_Big_Wheel_Sow_frame)
        self.add_explain(title='首页大轮播-外部链接', address='http://www.eslink.cc', image=5, rank=1, explain='自动创建-商品列表')
        page_Refresh(self, Home_Big_Wheel_Sow_path().close_menu)
        Selection_Menu(self, Home_Management_path().Home_Big_Wheel_Sow)
        is_frame_page(self, Home_Management_frame().Home_Big_Wheel_Sow_frame)
        self.add_internal_activity(title='首页大轮播-内部链接-活动详情', image=6, rank=2, explain='自动创建-活动详情')
        page_Refresh(self, Home_Big_Wheel_Sow_path().close_menu)
        Selection_Menu(self, Home_Management_path().Home_Big_Wheel_Sow)
        is_frame_page(self, Home_Management_frame().Home_Big_Wheel_Sow_frame)
        self.add_internal_product_list(title='首页大轮播-内部链接-商品列表', one_level=1, two_level=1, image=7, rank=3, explain='自动创建-商品列表')
        page_Refresh(self, Home_Big_Wheel_Sow_path().close_menu)
        Selection_Menu(self, Home_Management_path().Home_Big_Wheel_Sow)
        is_frame_page(self, Home_Management_frame().Home_Big_Wheel_Sow_frame)
        self.add_internal_product_details(title='首页大轮播-内部链接-商品详情', product=1, image=8, rank=4, explain='自动创建-商品详情')

    @unittest.skip('无条件跳过')
    def test_delete_Home_Big_Wheel_Sow(self):
        u"""删除首页轮播（大）"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Home_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Home_Management_path().Home_Big_Wheel_Sow)
        is_frame_page(self, Home_Management_frame().Home_Big_Wheel_Sow_frame)
        self.delete_Home_Big_Wheel_Sow()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
