# coding=utf-8
"""
Created on 2019-04-03
@author: Four
Project: operation-商品信息
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
from Utils.DriverWait import Wait_Find, Wait_Click, Send_Key, Send_Picture, Wait_Text_present
logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间


class Product_Information(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def Add_product_information(self):
        """添加商品基本信息"""
        try:
            Wait_Click(self.browser, Product_Information_path().Add_Product)
            Wait_Click(self.browser, Add_product_information_path().goods_category)
            Wait_Click(self.browser, Add_product_information_path().one_category)
            Wait_Click(self.browser, Add_product_information_path().two_category)
            Send_Key(self.browser, Add_product_information_path().goods_title, "苏泊尔(SUPOR)QS505燃气灶")
            Send_Key(self.browser, Add_product_information_path().goods_number, "QS505")
            Send_Key(self.browser, Add_product_information_path().subhead, "苏泊尔(SUPOR)QS505燃气灶")
            Wait_Click(self.browser, Add_product_information_path().logistics)
            Wait_Click(self.browser, Add_product_information_path().logistics_status % format(1))
            time.sleep(0.5)
            Wait_Click(self.browser, Add_product_information_path().product_label)
            Wait_Click(self.browser, Add_product_information_path().label_no % format(2))
            Send_Key(self.browser, Add_product_information_path().remark, "自动创建商品")
            Send_Picture(self.browser, Add_product_information_path().product_carousel, Add_product_information_path().carousel_product % format(1))
            Wait_Find(self.browser, (By.XPATH, Product_Information_path().Prompt_Message))
            Send_Picture(self.browser, Add_product_information_path().product_details, Add_product_information_path().carousel_product % format(2))
            Wait_Find(self.browser, (By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[12]/div/div/div/div[1]/img"))
            self.browser.find_element_by_xpath(Add_product_information_path().save_button).click()
            time.sleep(3)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Add_product_parameters(self, name, value):
        u"""添加商品参数"""
        try:
            Wait_Find(self.browser, (By.XPATH, Add_product_parameters_path().parameter_name))
            self.browser.find_element_by_xpath(Add_product_parameters_path().parameter_name).send_keys(name)
            self.browser.find_element_by_xpath(Add_product_parameters_path().parameter_value).send_keys(value)
            Wait_Click(self.browser, Add_product_parameters_path().save_button)
            Wait_Find(self.browser, (By.XPATH, Add_product_specification_path().goods_specification_menu))
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Add_product_specification(self, name, value1, value2):
        u"""添加商品规格"""
        try:
            Wait_Click(self.browser, Add_product_specification_path().goods_specification_menu)
            time.sleep(0.5)
            Wait_Click(self.browser, Add_product_specification_path().add_specification)
            Send_Key(self.browser, Add_product_specification_path().specification_name, name)
            Send_Key(self.browser, Add_product_specification_path().specification_value % format(1), value1)
            Wait_Click(self.browser, Add_product_specification_path().add_specification_value)
            Send_Key(self.browser, Add_product_specification_path().specification_value % format(2), value2)
            Wait_Click(self.browser, Add_product_specification_path(). ensure_button)
            Wait_Find(self.browser, (By.XPATH, Add_product_stock_path().product_stock_menu))
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Add_product_stock(self, sales, cost, market, integral, stock):
        u"""添加商品库存"""
        try:
            Wait_Click(self.browser, Add_product_stock_path().product_stock_menu)
            Wait_Click(self.browser, Add_product_stock_path().add_stock)
            Wait_Click(self.browser, Add_product_stock_path().product_specification)
            Wait_Click(self.browser, Add_product_stock_path().specification_value % format(1))
            Send_Key(self.browser, Add_product_stock_path().sales_price, sales)
            Send_Key(self.browser, Add_product_stock_path().cost_price, cost)
            Send_Key(self.browser, Add_product_stock_path().market_price, market)
            Send_Picture(self.browser, Add_product_stock_path().product_images, Add_product_stock_path().carousel_product % format(1))
            Wait_Find(self.browser, (By.XPATH, Product_Information_path().Prompt_Message))
            Wait_Click(self.browser, Add_product_stock_path().product_status % format(1))
            Send_Key(self.browser, Add_product_stock_path().integral, integral)
            Send_Key(self.browser, Add_product_stock_path().stock, stock)
            Wait_Click(self.browser, Add_product_stock_path().save_button)
            Wait_Click(self.browser, Product_Information_path().Quit)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Choose_product_information(self):
        u"""选择商品信息"""
        try:
            Wait_Click(self.browser, Product_Information_path().Choose % format(1))
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Delete_product_information(self):
        u"""删除商品信息"""
        try:
            Wait_Click(self.browser, Product_Information_path().Delete_Product)
            Wait_Click(self.browser, Product_Information_path().Delete_ensure)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Grounding_product_information(self):
        u"""上架商品"""
        try:
            Wait_Click(self.browser, Product_Information_path().Grounding_Button)
            Wait_Text_present(self.browser, Product_Information_path().Grounding_Status % format(1), "上架")
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            return False

    def Query_product_information(self, product_name='', product_number=''):
        u"""查询商品信息"""
        try:
            Wait_Click(self.browser, Product_Information_path().query_product_classify)
            Wait_Click(self.browser, Product_Information_path().query_product_classify_list)
            Wait_Click(self.browser, Product_Information_path().query_product_classify_value)
            Send_Key(self.browser, Product_Information_path().query_product_name, product_name)
            Send_Key(self.browser, Product_Information_path().query_product_number, product_number)
            Wait_Click(self.browser, Product_Information_path().Query_Button)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Undercarriage_product_information(self):
        u"""下架商品"""
        try:
            Wait_Click(self.browser, Product_Information_path().Undercarriage_Button)
            Wait_Text_present(self.browser, Product_Information_path().Grounding_Status % format(1), "下架")
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    # @unittest.skip('无条件跳过')
    def test_Product_Classify(self):
        u"""商品信息"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Product_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Product_Management_path().Product_Message)
        is_frame_page(self, Product_Management_frame().Product_Message_frame)
        # 添加商品
        self.Add_product_information()
        self.Add_product_parameters(name="品牌", value="苏泊尔")
        self.Add_product_specification(name="商品颜色", value1="贵族金", value2="天空蓝")
        self.Add_product_stock(sales='1888', cost='1688', market='2088', integral='1888', stock='0')
        # 删除商品
        # self.Delete_product_information()
        # 上下架
        # self.Choose_product_information()
        # self.Grounding_product_information()
        # self.Choose_product_information()
        # self.Undercarriage_product_information()
        # 查询
        self.Query_product_information()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
