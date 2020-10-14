# -*- coding: utf-8 -*-
"""
Created on 2018-03-22
@author: sun
Project:下拉框选择
"""
from Utils.log import Logger
import time, sys

send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  #获取当前时间
logger_message = Logger()


def is_pull_down_list(browser,locator,message):
    u"""下拉选择"""
    try:
        list_temp = browser.find_elements_by_xpath(locator)
        for li in list_temp:
            print(li)
            if message in li.text:
                logger_message.loginfo('%s\t方法名：%s \t选择参数：%s' % (send_time, sys._getframe().f_code.co_name, li.text))
                li.click()
                break
    except Exception as is_pull_down_list_error:

            print(u"%s\t方法名：%s\t下拉选择-异常:%s" % (send_time,sys._getframe().f_code.co_name,is_pull_down_list_error))
            #
            # logger_message.logwarning(u"%s\t方法名：%s\t下拉选择-异常:%s" % (send_time,sys._getframe().f_code.co_name,is_pull_down_list_error))


