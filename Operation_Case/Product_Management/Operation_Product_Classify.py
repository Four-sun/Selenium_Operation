# coding=utf-8
"""
Created on 2019-04-01
@author: Four
Project: operation-商品分类
"""
import sys
import time
import unittest
from Utils.log import Logger
from selenium import webdriver
from Constant.Constant_Path import *
from Utils.DriverWait import Wait_Find
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utils.Login_User import login_user,Operation_Center
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from Utils.Selection_Menu import Fixed_Window, is_frame_page, Selection_Menu

logger_message = Logger()
send_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间
Refresh_Button = ".//*[@id='userManage']/div/div/div/div[1]/div/i"  # 刷新
Prompt_Message = '/html/body/div[5]/div/div/div[1]/div/span'    # 提示
Add_Button = '//*[@id="userManage"]/div/div/div/form/div/div/button/span'   # 添加
Class_Name = '/html/body/div[4]/div[2]/div/div/div[2]/form/div/div[1]/div[1]/div/div[1]/input'  # 商品分类
Category_Parent = '/html/body/div[4]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/div/div/div[1]/div/span'  # 上级分类
Category_Images = '/html/body/div[4]/div[2]/div/div/div[2]/form/div/div[2]/div/div/div/div/div/input'   # 分类图片
Image_Path = 'C:\\Users\\Administrator\\Desktop\\eslink\\云商城\图片\\UI设计\\图标\\燃气灶.png'         # 图片地址
Image_Delete = 'html/body/div[4]/div[2]/div/div/div[2]/form/div/div[2]/div/div/div[1]/div[1]/div/div[1]/i[2]'   # 图片删除
Image_Preview = 'html/body/div[4]/div[2]/div/div/div[2]/form/div/div[2]/div/div/div[1]/div[1]/div/div[1]/i[1]'  # 图片预览
Ok_Button = '/html/body/div[4]/div[2]/div/div/div[3]/div/button[2]/span'        # 添加确定按钮
Cancel_Button = '/html/body/div[4]/div[2]/div/div/div[3]/div/button[1]/span'    # 添加取消按钮
Get_Class_Name = '//*[@id="userManage"]/div/div/div/div[2]/div[2]/div[9]/div[1]/span[1]'        # 获取类名
Get_Number = '//*[@id="userManage"]/div/div/div/div[2]/div[2]/div[%s]/div[1]/span[1]'       # 获取数量
First_Image = '/html/body/div[4]/div[2]/div/div/div[2]/form/div/div[2]/div/div/div[1]/div[1]/img'
Modify_Button = ".//*[@id='userManage']/div/div/div/div[2]/div[2]/div[%s]/div[1]/span[2]/span[1]"       # 修改按钮
Stick_Button = ".//*[@id='userManage']/div/div/div/div[2]/div[2]/div[%s]/div[1]/span[2]/span[2]"        # 置顶按钮
subclass_path = ".//*[@id='userManage']/div/div/div/div[2]/div[2]/div[%s]/div[1]/span[2]/span[4]"       # 新增二级分类
One_Delete_Button = ".//*[@id='userManage']/div/div/div/div[2]/div[2]/div[%s]/div[1]/span[2]/span[3]"     # 一级分类删除按钮
Two_Delete_Button = ".//*[@id='userManage']/div/div/div/div[2]/div[2]/div[%s]/div[2]/div/div/p/span[2]/span[3]" # 二级分类删除按钮
Unfold_Button = ".//*[@id='userManage']/div/div/div/div[2]/div[2]/div[10]/div[1]/i"   # 展开按钮
Delete_Ensure = "html/body/div[2]/div[2]/div/div/div[3]/div/button[2]"  # 删除确定


class Product_Classify(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.option = webdriver.ChromeOptions()
        cls.option.add_argument('disable-infobars')
        cls.browser = webdriver.Chrome(options=cls.option)
        cls.browser.maximize_window()
        cls.browser.get(Constant_path().LOGIN_URL)

    def get_div_number(self, product):
        Wait_Find(self.browser, (By.XPATH, Add_Button))
        for i in range(10):
            number = i+1
            class_number = '//*[@id="userManage"]/div/div/div/div[2]/div[2]/div[%s]/div[1]/span[1]' % number
            self.browser.implicitly_wait(5)
            number_text = self.browser.find_element_by_xpath(class_number).text
            if number_text == '分类名称：%s' % product:
                return int(number)
            else:
                # print('未找到元素')
                continue
        time.sleep(0.5)

    def Add_one_product_classification(self):
        u"""新增一级商品分类"""
        try:
            get_class_no = self.get_div_number(product="燃气灶")
            if get_class_no >= 1:
                logger_message.loginfo('分类已存在!')
        except NoSuchElementException:
            Wait_Find(self.browser, (By.XPATH, Add_Button))
            self.browser.find_element_by_xpath(Add_Button).click()
            self.browser.find_element_by_xpath(Class_Name).send_keys('燃气灶')
            self.browser.find_element_by_xpath(Category_Images).send_keys(Image_Path)
            Wait_Find(self.browser, (By.XPATH, Prompt_Message))
            self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '上传成功', msg='图片上传失败')
            self.browser.find_element_by_xpath(Ok_Button).click()
            logger_message.loginfo('分类创建成功!')

    def Required_fields_check(self, case):
        u"""新增商品分类必填项检查"""
        try:
            Wait_Find(self.browser, (By.XPATH, Add_Button))
            self.browser.find_element_by_xpath(Add_Button).click()
            if case == 1:       # 全部不输点击确定
                self.browser.find_element_by_xpath(Ok_Button).click()
                self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '请输入分类名称', msg='请输入分类名称错误!')
            elif case == 2:     # 输入分类名称不上传照片
                self.browser.find_element_by_xpath(Class_Name).send_keys('燃气灶')
                self.browser.find_element_by_xpath(Ok_Button).click()
                self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '请上传分类图片', msg='请上传分类图片错误!')
            elif case == 3:     # 上传照片但不输入分类名称
                self.browser.find_element_by_xpath(Category_Images).send_keys(Image_Path)
                Wait_Find(self.browser, (By.XPATH, Prompt_Message))
                self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '上传成功', msg='图片上传失败')
                self.browser.find_element_by_xpath(Ok_Button).click()
                self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '请输入分类名称', msg='请输入分类名称错误!')
            elif case == 4:     # 输入分类名称字符过长
                self.browser.find_element_by_xpath(Class_Name).send_keys('测试下商品分类问题字符长度问题')
                self.browser.find_element_by_xpath(Ok_Button).click()
                self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '分类名称最大长度为4', msg='分类名称最大长度为4错误!')
            elif case == 5:     # 检查图片删除二次上传是否正确
                    self.browser.find_element_by_xpath(Category_Images).send_keys(Image_Path)
                    Wait_Find(self.browser, (By.XPATH, First_Image))
                    self.browser.find_element_by_xpath(First_Image).click()
                    self.browser.find_element_by_xpath(Image_Delete).click()
                    self.browser.find_element_by_xpath(Category_Images).send_keys(Image_Path)
                    Wait_Find(self.browser, (By.XPATH, Image_Delete))
                    self.browser.find_element_by_xpath(Image_Delete).click()
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Add_two_product_classification(self):
        """新增二级商品分类"""
        try:
            get_class_no = self.get_div_number(product='燃气灶')
            self.browser.find_element_by_xpath(subclass_path % format(get_class_no)).click()
            self.browser.implicitly_wait(5)
            self.browser.find_element_by_xpath(Class_Name).send_keys('燃气灶')
            self.browser.find_element_by_xpath(Category_Images).send_keys(Image_Path)
            # time.sleep(2)
            Wait_Find(self.browser, (By.XPATH, Prompt_Message))
            self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '上传成功', msg='图片上传失败')
            # time.sleep(2)
            self.browser.find_element_by_xpath(Ok_Button).click()
            try:
                self.browser.find_element_by_xpath(Cancel_Button).click()
                time.sleep(1)
            except NoSuchElementException:
                pass
                logger_message.loginfo('二级分类创建成功!')
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Stick_product_classification(self):
        """置顶分类"""
        try:
            get_class_no = self.get_div_number(product='燃气灶')
            self.browser.find_element_by_xpath(Stick_Button % format(get_class_no)).click()
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def Delete_product_classification(self, case):
        """删除分类"""
        try:
            get_class_no = self.get_div_number(product='燃气灶')
            if case == 1:   # 删除一级分类
                self.browser.find_element_by_xpath(One_Delete_Button % format(get_class_no)).click()
                self.browser.find_element_by_xpath(Delete_Ensure).click()
                Wait_Find(self.browser, (By.XPATH, Prompt_Message))
                logger_message.loginfo(self.browser.find_element_by_xpath(Prompt_Message).text)
            elif case == 2:     # 删除二级分类
                self.browser.find_element_by_xpath(Unfold_Button).click()
                Wait_Find(self.browser, (By.XPATH, Two_Delete_Button % format(get_class_no)))
                self.browser.find_element_by_xpath(Two_Delete_Button % format(get_class_no)).click()
                self.browser.find_element_by_xpath(Delete_Ensure).click()
                Wait_Find(self.browser, (By.XPATH, Prompt_Message))
                self.assertEqual(self.browser.find_element_by_xpath(Prompt_Message).text, '删除成功', msg='删除成功失败!')
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    # @unittest.skip('无条件跳过')
    def test_Product_Classify(self):
        u"""商品分类"""
        login_user(self, LoginName=u'zhangyang1', LoginPwd=u"960418")
        Operation_Center(self)
        Fixed_Window(self)
        Selection_Menu(self, Operation_path().Product_Management)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()
        Selection_Menu(self, Product_Management_path().Product_Classify)
        is_frame_page(self, Product_Management_frame().Product_Classify_frame)
        # self.get_div_number()
        # self.Required_fields_check(case=5)
        self.Add_one_product_classification()
        self.Add_two_product_classification()
        self.Stick_product_classification()
        # self.Delete_product_classification(case=1)
        # self.Delete_product_classification(case=2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        # cls.browser.quit()

if __name__ == "__main__":
    unittest.main()
