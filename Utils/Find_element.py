# coding=utf-8
"""
Created on 2019-04-04
@author: Four
Project: 基于原生的selenium框架做二次封装
"""
from selenium import webdriver
from selenium.common.exceptions import *   # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator, timeout=10):
        """定位元素方法封装"""
        element = WebDriverWait(self.browser, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def click(self, locator):
        """点击操作"""
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """发送文本，清空后输入"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
