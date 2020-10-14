# -*- coding: utf-8 -*-
"""
@Time:2019-04-01
constant/Constant_Path.py
常量部分（固定不变使用频繁的参数维护在此处）
"""


class Constant_path(object):
    u"""url地址"""
    def __init__(self):
        self.LOGIN_URL = "http://etbc-qa.eslink.net.cn/"


class Error_Picture_path(object):
    u"""错误截图地址"""
    def __init__(self):
        self.Picture_path = "D:\\pycharm-5.0.4\\Selenium_cloudwork\\Error_picture\\"


class Operation_path(object):
    u"""商城管理一级菜单Xpath地址"""
    def __init__(self):
        self.Product_Management = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[1]/li/div'            # 商品管理
        self.Transaction_Management = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[2]/li/div'        # 交易管理
        self.Home_Management = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[3]/li/div'               # 首页管理
        self.Member_Management = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[4]/li/div'             # 会员管理
        self.Production_Management = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[5]/li/div'         # 运营管理


class Product_Management_path(object):
    u"""商品管理二级菜单Xpath地址"""
    def __init__(self):
        self.Product_Classify = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[1]/li/ul/li[1]'      # 商品分类
        self.Product_Message = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[1]/li/ul/li[2]'       # 商品信息
        self.Product_Stock = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[1]/li/ul/li[3]'         # 商品库存
        self.Product_Evaluate = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[1]/li/ul/li[4]'      # 商品评价
        self.Product_Statistics = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[1]/li/ul/li[5]'    # 商品统计


class Product_Management_frame(object):
    u"""商品管理二级菜单frame地址"""
    def __init__(self):
        self.Product_Classify_frame = 'personalpage_01320101'       # 商品分类
        self.Product_Message_frame = 'personalpage_01320102'        # 商品信息
        self.Product_Stock_frame = 'personalpage_01320103'          # 商品库存
        self.Product_Evaluate_frame = 'personalpage_01320104'       # 商品评价
        self.Product_Statistics_frame = 'personalpage_01320105'     # 商品统计


class Transaction_Management_path(object):
    u"""交易管理二级菜单Xpath地址"""
    def __init__(self):
        self.Transaction_Information = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[2]/li/ul/li[1]'      # 交易信息
        self.Trade_Statistic = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[2]/li/ul/li[2]'              # 交易统计


class Transaction_Management_frame(object):
    u"""交易管理二级菜单frame地址"""
    def __init__(self):
        self.Transaction_Information_frame = 'personalpage_01320201'         # 交易信息
        self.Trade_Statistic_frame = 'personalpage_01320202'                 # 交易统计


class Home_Management_path(object):
    u"""首页管理二级菜单Xpath地址"""
    def __init__(self):
        self.Home_Big_Wheel_Sow = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[3]/li/ul/li[1]'        # 首页大轮播
        self.Home_Small_Wheel_Sow = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[3]/li/ul/li[2]'      # 首页小轮播
        self.Home_Menu = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[3]/li/ul/li[3]'                 # 首页菜单
        self.Home_Tag = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[3]/li/ul/li[4]'                # 首页标签
        self.Home_Notice = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[3]/li/ul/li[5]'               # 首页公告


class Home_Management_frame(object):
    u"""首页管理二级菜单frame地址"""
    def __init__(self):
        self.Home_Big_Wheel_Sow_frame = 'personalpage_01320301'        # 首页大轮播
        self.Home_Small_Wheel_Sow_frame = 'personalpage_01320302'      # 首页小轮播
        self.Home_Menu_frame = 'personalpage_01320303'                 # 首页菜单
        self.Home_Tag_frame = 'personalpage_01320304'                  # 首页标签
        self.Home_Notice_frame = 'personalpage_01320305'               # 首页公告


class Member_Management_path(object):
    u"""会员管理二级菜单Xpath地址"""
    def __init__(self):
        self.Member_Information = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[4]/li/ul/li'         # 会员信息


class Member_Management_frame(object):
    u"""会员管理二级菜单frame地址"""
    def __init__(self):
        self.Member_Information_frame = 'personalpage_01320401'         # 会员信息


class Production_Management_path(object):
    u'''运营管理二级菜单Xpath地址'''
    def __init__(self):
        self.Activity = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[5]/li/ul/li[1]'              # 活动
        self.Discount_Coupon = '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/ul[5]/li/ul/li[2]'       # 优惠券


class Production_Management_frame(object):
    u"""运营管理二级菜单frame地址"""
    def __init__(self):
        self.Activity_frame = 'personalpage_01320501'                      # 活动
        self.Discount_Coupon_frame = 'personalpage_01320502'               # 优惠券
