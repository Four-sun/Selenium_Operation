# coding=utf-8
"""
Created on 2019-04-01
@author: Four
Project: 选择菜单
"""

import sys
import time
from Utils.log import Logger
from Utils.DriverWait import Wait_Find
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains as AC

send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
logger_message = Logger()


def Selection_Menu(self ,Menu_path):
    u"""选择菜单"""
    try:
        Wait_Find(self.browser, (By.XPATH, Menu_path))
        self.browser.find_element_by_xpath(Menu_path).click()
        time.sleep(0.5)
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t菜单异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def Fixed_Window(self):
    u"""窗口固定按钮"""
    try:
        Fixed_Window_Xpath = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/h3/p'
        Wait_Find(self.browser, (By.XPATH, Fixed_Window_Xpath))
        self.browser.find_element_by_xpath(Fixed_Window_Xpath).click()
    except Exception as Fixed_Window_error:
        logger_message.logwarning(u"%s\t方法名：%s\t窗口固定按钮-异常：%s" % (send_time, sys._getframe().f_code.co_name, Fixed_Window_error))
        raise


def is_frame_page(self,page):
    u"""frame页面"""
    try:
        self.browser.implicitly_wait(10)
        self.browser.switch_to.frame(self.browser.find_element_by_id(page))
        logger_message.loginfo(u"%s\t方法名：%s\t切换frame页面" % (send_time, sys._getframe().f_code.co_name))
    except Exception as frame_page_error:
        logger_message.logwarning(u"%s\t方法名：%s\t切换frame页面-异常：%s" % (send_time, sys._getframe().f_code.co_name, frame_page_error))
        raise




