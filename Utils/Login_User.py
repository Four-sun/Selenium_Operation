# -*- coding: utf-8 -*-
"""
Created on 2019-01-07
@author: sun
Project: 登陆etbc后台
"""

import sys
import time
from Utils.log import Logger
from Utils.DriverWait import Wait_Find
from Utils.ScreenShot import Screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))     # 获取当前时间
logger_message = Logger()


def login_user(self, LoginName, LoginPwd):

    u"""这里写了一个登录的方法,账号和密码参数化"""
    try:
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div/div/input').clear()
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div/div/input').send_keys(LoginName)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/div/input').clear()
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/div/input').send_keys(LoginPwd)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div/button').click()
        self.browser.implicitly_wait(30)
        logger_message.loginfo(u'%s\t方法名：%s\t登录帐号：%s\t密码：%s' % (send_time, sys._getframe().f_code.co_name, LoginName,LoginPwd))
    except Exception as login_user_Error:
        Screenshot(self, u'登录帐号密码异常')
        logger_message.logwarning(u"%s\t方法名：%s\t登录帐号密码异常：%s" % (send_time, sys._getframe().f_code.co_name, login_user_Error))
        raise


def Operation_Center(self, Number=31):
    u"""云商城菜单"""
    try:
        xpath = '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/ul/li[1]'           # 先选择第一个菜单进行定位，为后续的键盘操作定位元素
        Wait_Find(self.browser, (By.XPATH, xpath))
        self.browser.find_element_by_xpath(xpath).click()
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()              # 使用ActionChains未选取元素进行键盘操作
        Operation_Center_xpath = '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/ul/li[%s]' % Number
        Wait_Find(self.browser, (By.XPATH, Operation_Center_xpath))
        self.browser.find_element_by_xpath(Operation_Center_xpath).click()
    except Exception as Operation_Center_Error:
        logger_message.logwarning(u"%s\t方法名：%s\t云商城菜单异常%s" % (send_time, sys._getframe().f_code.co_name, Operation_Center_Error))
        raise

