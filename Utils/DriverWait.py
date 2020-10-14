# -*- coding: utf-8 -*-
"""
@Time:2019-01-09
@author: Four
Project:WebDriverWait和expected_conditions判断元素方法
"""

import sys
import time
import datetime
from Utils.log import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))     # 获取当前时间
logger_message = Logger()


def Wait_Find(browser, locator, timeout=10):
    """
    定位元素，参数locator是元祖类型,
    By要引包 from selenium.webdriver.common.by import By
    如(By.XPATH, "//*[@id="app"]/div")
    """
    try:
        element = WebDriverWait(browser, timeout).until(EC.presence_of_element_located(locator))
        time.sleep(0.5)
        return element
    except Exception as Find_Error:
        logger_message.logwarning(u"%s\t方法名：%s\t未找到元素异常%s" % (send_time, sys._getframe().f_code.co_name, Find_Error))
        raise


def Wait_Text_present(browser, locator, Text, timeout=5):
    """
    判断指定的元素中是否包含了预期的字符串，返回布尔值
    """
    try:
        locator_xpath = (By.XPATH, locator)
        WebDriverWait(browser, timeout).until(EC.text_to_be_present_in_element((locator_xpath), Text))
        time.sleep(0.5)
        return True
    except Exception as Find_Error:
        logger_message.logwarning(u"%s\t方法名：%s\t未找到元素异常%s" % (send_time, sys._getframe().f_code.co_name, Find_Error))
        return False


def Wait_Until(browser, locator, timeout=10):
    """
    # 等待时长10秒，默认0.5秒询问一次
    """
    try:
        element = WebDriverWait(browser, timeout).until(lambda x: x.find_element_by_xpath(locator))
        time.sleep(1)
        return element
    except Exception as Find_Error:
        logger_message.logwarning(u"%s\t方法名：%s\t未找到元素异常%s" % (send_time, sys._getframe().f_code.co_name, Find_Error))
        raise


def Wait_Click(browser, locator, timeout=10):
    """
    element_to_be_clickable : 判断某个元素中是否可见并且是enable的，这样的话才叫 clickable
    """
    try:
        locator_path = (By.XPATH, locator)
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located(locator_path))
        browser.find_element_by_xpath(locator).click()
        time.sleep(0.5)
    except Exception as Find_Error:
        logger_message.logwarning(u"%s\t方法名：%s\t未找到元素异常%s" % (send_time, sys._getframe().f_code.co_name, Find_Error))
        raise


def Send_Key(browser, locator, text):
    """
    发送文本，清空后输入
    """
    try:
        element = browser.find_element_by_xpath(locator)
        time.sleep(0.5)
        element.clear()
        element.send_keys(text)
    except Exception as Find_Error:
        logger_message.logwarning(u"%s\t方法名：%s\t未找到元素异常%s" % (send_time, sys._getframe().f_code.co_name, Find_Error))
        raise


def Send_Picture(browser, locator, text):
    """
    上传发送图片
    """
    try:
        time.sleep(0.5)
        element = browser.find_element_by_xpath(locator)
        element.send_keys(text)
    except Exception as Find_Error:
        logger_message.logwarning(u"%s\t方法名：%s\t未找到元素异常%s" % (send_time, sys._getframe().f_code.co_name, Find_Error))
        raise


def Calculate_inventory(browser,type, last, this, number):
    """
    计算库存量
    """
    try:
        time.sleep(0.5)
        Last_inventory = browser.find_element_by_xpath(last).text
        This_inventory = browser.find_element_by_xpath(this).text
        in_and_out_inventory = browser.find_element_by_xpath(number).text
        if type == 0:
            if int(This_inventory) - int(Last_inventory) == int(in_and_out_inventory):
                logger_message.loginfo("入库数量计算正确")
                return True
            else:
                logger_message.loginfo('入库数量计算错误')
                return False
        elif type == 1:
            if int(Last_inventory) - int(This_inventory) == int(in_and_out_inventory):
                logger_message.loginfo("出库数量计算正确")
                return True
            else:
                logger_message.loginfo('出库数量计算错误')
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t未找到元素异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def page_Refresh(self, close_menu):
    u"""页面刷新"""
    try:
        time.sleep(0.5)
        self.browser.switch_to.default_content()
        time.sleep(0.5)
        ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath(close_menu)).click().perform()
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def page_scrolling(self, scroll):
    u"""页面滚动"""
    try:
        time.sleep(0.5)
        if scroll == 0:
            ActionChains(self.browser).send_keys(Keys.PAGE_UP).perform()  # 向上滚动
        elif scroll == 1:
            ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()  # 向下滚动
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def public_time(days=1):
    u"""区域时间"""
    try:
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        get_time = (datetime.datetime.now()+datetime.timedelta(days)).strftime("%Y-%m-%d %H:%M:%S")
        interval_time = now_time + ' - ' + get_time
        return interval_time
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def select_list(self, get_list, name):
    try:
        get_text = self.browser.find_elements_by_xpath(get_list)
        for i in range(len(get_text)):
            get_name = get_text[i].text
            if get_name == name:
                get_text[i].click()
            else:
                pass
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise