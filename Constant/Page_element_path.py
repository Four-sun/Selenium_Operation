# -*- coding: utf-8 -*-
"""
@Time:2019-04-04
constant/Page_element_path.py
页面元素的地址维护
"""


class Product_Information_path(object):
    u"""商品信息首页信息元素地址"""
    def __init__(self):
        self.Prompt_Message = "/html/body/div[8]/div/div/div[1]/div/span"                                # 提示
        self.Refresh_Button = ".//*[@id='userManage']/div/div[1]/div/div[1]/div/i"                       # 刷新
        self.Reset_Button = ".//*[@id='userManage']/div/div[1]/div/form/div[1]/div[4]/button[1]"         # 重置
        self.Query_Button = ".//*[@id='userManage']/div/div[1]/div/form/div[1]/div[4]/button[2]"         # 查询
        self.Undercarriage_Button = ".//*[@id='userManage']/div/div[1]/div/form/div[2]/div/button[1]"    # 下架
        self.Grounding_Button = ".//*[@id='userManage']/div/div[1]/div/form/div[2]/div/button[2]"        # 上架
        self.Delete_Product = ".//*[@id='userManage']/div/div[1]/div/form/div[2]/div/button[3]"          # 删除
        self.Delete_ensure = "/html/body/div[7]/div[2]/div/div/div[3]/div/button"                        # 确定删除
        self.Add_Product = ".//*[@id='userManage']/div/div[1]/div/form/div[2]/div/button[4]"             # 添加
        self.Quit = "/html/body/div[4]/div[2]/div/div/a/i"                                               # 退出
        self.Grounding_Status = '//*[@id="userManage"]/div/div[1]/div/div[2]/div[1]/div/div[2]/table/tbody/tr[%s]/td[10]/div/span' # 上下架状
        self.Choose = './/*[@id="userManage"]/div/div[1]/div/div[2]/div[1]/div/div[2]/table/tbody/tr[%s]/td[1]/div/label/span/input'    # 选择商品
        self.Choose_all = ".//*[@id='userManage']/div/div[1]/div/div[2]/div[1]/div/div[1]/table/thead/tr[1]/th[1]/div/label/span/input" # 选择全部商品
        self.query_product_classify = ".//*[@id='userManage']/div/div[1]/div/form/div[1]/div[1]/div/div[1]/div[2]"                      # 查询商品分类
        self.query_product_classify_list = ".//*[@id='userManage']/div/div[1]/div/form/div[1]/div[1]/div/div[2]/div/span/ul/li[1]"      # 分类列表
        self.query_product_classify_value = ".//*[@id='userManage']/div/div[1]/div/form/div[1]/div[1]/div/div[2]/div/span/span/ul/li"  # 列表中第一个
        self.query_product_number = '//*[@id="userManage"]/div/div[1]/div/form/div[1]/div[2]/div/input'      # 商品编号
        self.query_product_name = '//*[@id="userManage"]/div/div[1]/div/form/div[1]/div[3]/div/input'       # 商品名称


class Add_product_information_path(object):
    u"""商品基本信息元素地址"""
    def __init__(self):
        self.cancel_button = "html/body/div[4]/div[2]/div/div/div[3]/div/button[1]"
        self.save_button = "html/body/div[4]/div[2]/div/div/div[3]/div/button[2]"
        self.goods_category = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div[1]/div[1]/input" # 商品分类
        self.one_category = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div[2]/div/span/ul/li[1]" # 一级分类
        self.two_category = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div[2]/div/span/span/ul/li" #二级分类
        self.goods_number = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[2]/div/div/div/input"# 编号
        self.goods_title = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[3]/div/div/div/input"  # 标题
        self.subhead = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[4]/div/div/div/input"  # 副标题
        self.weight = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[5]/div/div/div/div[2]/input"# 重量
        self.logistics = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[6]/div/div/div/div[1]/div/span" # 物流
        self.logistics_status = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/ul[2]/li[%s]" # 需要物流 1.需要 2.不需要
        self.product_type = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[7]/div/div/div/div[1]/div/span"   # 商品类型
        self.product_label = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[8]/div/div/div/div[1]/div/span"  # 商品标签
        self.label_no = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/ul[2]/li[%s]"   # 选择标签
        self.remark = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[9]/div/div/div/input"   # 备注
        self.product_carousel = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[11]/div/div/div/div/div/input"   # 商品轮播
        self.carousel_product = "D:\\pycharm-5.0.4\\Selenium_operation\\Data\\pro_%s.jpg"
        self.product_details = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/form/div/div[12]/div/div/div/div/div/input"   # 商品详情


class Add_product_parameters_path(object):
    """商品参数元素地址"""
    def __init__(self):
        self.parameter_name = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/input"    # 参数名
        self.parameter_value= "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/div/input"    # 参数值
        self.save_button = "html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/van-button"    # 保存


class Add_product_specification_path(object):
    u"""添加商品规格元素地址"""
    def __init__(self):
        self.goods_specification_menu = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[4]"  # 商品规格菜单
        self.add_specification = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div/button/span"   # 添加规格
        self.specification_name = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/input" # 规格名称
        self.specification_value = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[%s]/div/input"# 规格值
        self.add_specification_value = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/button"# 添加规格值
        self.cancel_button = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[2]/button[1]/span" # 取消
        self.ensure_button = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[2]/button[2]"  # 保存


class Add_product_stock_path(object):
    u"""添加商品库存元素地址"""
    def __init__(self):

        self.product_stock_menu = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[5]"  # 库存菜单
        self.add_stock = "/html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[1]/div/button"         # 添加库存
        self.product_specification = "/html/body/div[6]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div/div[1]/div/span"   # 商品规格
        self.specification_value = "/html/body/div[6]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div/div[2]/ul[2]/li[%s]" # 规格值
        self.sales_price = "html/body/div[6]/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div/div/div[2]/input"      # 销售价
        self.cost_price = "html/body/div[6]/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/div/div[2]/input"       # 成本价
        self.market_price = "html/body/div[6]/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div/div/div[2]/input"     # 市场价
        self.product_images = "/html/body/div[6]/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/div/input" # 商品图片
        self.product_status = "html/body/div[6]/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/div/label[%s]"  # 商品状态：1有效 2无效
        self.integral = "html/body/div[6]/div[2]/div/div/div[2]/form/div[4]/div[2]/div/div/div/div[2]/input"     # 获赠积分
        self.stock = "html/body/div[6]/div[2]/div/div/div[2]/form/div[5]/div[1]/div/div/div/div[2]/input"        # 库存数量
        self.save_button = "html/body/div[6]/div[2]/div/div/div[3]/div/button[2]"           # 保存按钮
        self.carousel_product = "D:\\pycharm-5.0.4\\Selenium_operation\\Data\\pro_%s.jpg"   # 商品图片


class Product_stock_path(object):
    u"""商品库存菜单元素地址"""
    def __init__(self):
        self.query_product_classify = '//*[@id="userManage"]/div/div[1]/div/form/div/div[1]/div/div[1]/div[2]'  # 查询商品分类
        self.query_product_classify_list = '//*[@id="userManage"]/div/div[1]/div/form/div/div[1]/div/div[2]/div/span/ul/li[2]'      # 分类列表
        self.query_product_classify_value = '//*[@id="userManage"]/div/div[1]/div/form/div/div[1]/div/div[2]/div/span/span/ul/li[1]'   # 列表中第一个
        self.query_product_name = '//*[@id="userManage"]/div/div[1]/div/form/div/div[2]/div/input'               # 商品名称
        self.query_button = '//*[@id="userManage"]/div/div[1]/div/form/div/div[3]/button/span'                   # 查询按钮
        self.choose_product = '//*[@id="tableheight"]/div[1]/div/div[2]/table/tbody/tr[%s]/td[8]/div/div/div'    # 选择商品库存管理
        self.in_and_out_management = '//*[@id="userManage"]/div/div[1]/div/div[3]/div[1]/div/div[2]/table/tbody/tr/td[9]/div/div/div'   # 出入库管理
        self.back_button = '//*[@id="userManage"]/div/div[1]/div/div[1]/button/span'                             # 返回按钮
        self.query_stock_number = '//*[@id="userManage"]/div/div[1]/div/form/div/div[1]/div/div[1]/div/span'     # 选择库存编号和规格
        self.query_stock_number_button = '//*[@id="userManage"]/div/div[1]/div/form/div/div[1]/div/div[2]/ul[2]/li[1]'      # 选择库存编号条件
        self.query_specification = '//*[@id="userManage"]/div/div[1]/div/form/div/div[1]/div/div[2]/ul[2]/li[2]' # 选择规格条件
        self.query_condition_send = '//*[@id="userManage"]/div/div[1]/div/form/div/div[2]/div/input'             # 库存编号和规格输入框
        self.current_stock = '//*[@id="EvaluateManage"]/div/div[1]/div/div[4]/div[1]/div/div[2]/table/tbody/tr[1]/td[4]/div/span'  #当前库存值
        self.in_storage = '//*[@id="EvaluateManage"]/div/div[1]/div/div[3]/button[2]'                           # 入库
        self.out_storage = '//*[@id="EvaluateManage"]/div/div[1]/div/div[3]/button[1]'                          # 出库
        self.in_and_out_number = '/html/body/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/input'          # 出入库数量
        self.in_and_out_remark = '/html/body/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/textarea'           # 出入库备注
        self.in_and_out_ensure_button = '/html/body/div[2]/div[2]/div/div/div[2]/div/button[2]/span'        # 出入库保存
        self.in_and_out_cancel_button = '/html/body/div[2]/div[2]/div/div/div[2]/div/button[1]/span'        # 出入库取消
        self.Last_inventory = '//*[@id="EvaluateManage"]/div/div[1]/div/div[4]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div/span'   # 上次库存量
        self.This_inventory = '//*[@id="EvaluateManage"]/div/div[1]/div/div[4]/div[1]/div/div[2]/table/tbody/tr[1]/td[4]/div/span'      # 本次库存量
        self.in_and_out_inventory = '//*[@id="EvaluateManage"]/div/div[1]/div/div[4]/div[1]/div/div[2]/table/tbody/tr[1]/td[3]/div/span'    # 出入库数量


class Product_evaluate_path(object):
    u"""商品评价菜单元素地址"""
    def __init__(self):
        self.choose_product = ".//*[@id='EvaluateManage']/div/div[1]/div/div[2]/div[1]/div/div[2]/table/tbody/tr[%s]/td[9]/div/div/div" #选择审核
        self.visible = "html/body/div[2]/div[2]/div/div/div[1]/div[3]/div/label[%s]/span/input"     # 1显示 2不显示
        self.response = "html/body/div[2]/div[2]/div/div/div[1]/div[4]/div[2]/textarea"     # 回复内容
        self.ensure_button = '/html/body/div[2]/div[2]/div/div/div[2]/div/button[2]/span'   # 确定按钮
        self.cancel_button = "/html/body/div[2]/div[2]/div/div/div[2]/div/button[1]/span"   # 取消按钮
        self.prompt_message = 'html/body/div[3]/div/div/div[1]/div/span'                    # 提示信息


class Transaction_information_path(object):
    u"""交易信息菜单元素地址"""
    def __init__(self):
        self.query_order_number = '//*[@id="userManage"]/div/div[1]/div/form/div/div[1]/div/input'    # 订单号
        self.query_mobile = '//*[@id="userManage"]/div/div[1]/div/form/div/div[2]/div/input'          # 手机号
        self.query_consignee = '//*[@id="userManage"]/div/div[1]/div/form/div/div[3]/div/input'       # 收货人
        self.query_order_status = '//*[@id="userManage"]/div/div[1]/div/form/div/div[4]/div/div[1]/div/span'  # 收货状态
        self.status = '//*[@id="userManage"]/div/div[1]/div/form/div/div[4]/div/div[2]/ul[2]/li[%s]'  # 状态列表
        self.query_order_time = '//*[@id="userManage"]/div/div[1]/div/form/div/div[5]/div/div[1]/div/input'   # 下单时间区间
        self.query_button = '//*[@id="userManage"]/div/div[1]/div/form/div/button[1]/span'      # 查询按钮
        self.export_button = '//*[@id="userManage"]/div/div[1]/div/form/div/button[2]/span'     # 导出按钮
        self.refund_audit = '//*[@id="userManage"]/div/div[1]/div/div[2]/div[1]/div/div[2]/table/tbody/tr[%s]/td[8]/div/div/span[3]'    # 退款审核
        self.refund_button = '//*[@id="userManage"]/div/div[1]/div/div[3]/div/div/div[2]/div[3]/div/div/div[3]/span[2]'# 退货页面退款按钮
        self.refund_agree = '//*[@id="orderdetailModal"]/div[2]/div/div/div[2]/div/div/label[1]/span/input'     # 同意退款
        self.refund_refuse = '//*[@id="orderdetailModal"]/div[2]/div/div/div[2]/div/div/label[2]/span/input'    # 拒绝退款
        self.refund_ensure_button = '//html/body/div[4]/div[2]/div/div/div[3]/div/button[2]/span'               # 退款确认按钮
        self.audit_ensure_button = '//*[@id="orderdetailModal"][1]/div[2]/div/div/div[3]/div/button[2]/span'    # 审核确认按钮
        self.audit_cancel_button = '//*[@id="orderdetailModal"]/div[2]/div/div/div[3]/div/button[1]/span'       # 审核取消按钮
        self.transaction_details = '//*[@id="userManage"]/div/div[1]/div/div[2]/div[1]/div/div[2]/table/tbody/tr[%s]/td[8]/div/div/span[1]' # 交易详情
        self.return_record_menu = '//*[@id="userManage"]/div/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div[4]'    # 退货记录页面
        self.delivery_button = '//*[@id="userManage"]/div/div[1]/div/div[2]/div[1]/div/div[2]/table/tbody/tr[%s]/td[8]/div/div/span[2]'     # 发货按钮
        self.record_delivery_button = '//*[@id="userManage"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/button/span'               # 发货记录中的发货按钮
        self.site = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/div/div[1]/div/span'              # 网点
        self.site_list = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/div/div[2]/ul[2]/li[%s]'     # 网点列表
        self.logistics_company = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[1]/div/span' # 物流公司
        self.logistics_company_list = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[2]/ul[2]/li[%s]' # 物流公司列表
        self.logistics_number = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[3]/div/input'            # 物流单号
        self.consignee = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[4]/div/input'# 收货人
        self.postcode = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[1]/div/input' #  邮编
        self.phone = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input'    # 电话
        self.area = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[3]/div/div[1]/div[1]/input'  # 地区
        self.detailed_address = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/div/input'       # 详细地址
        self.remark = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/form/div[4]/div/div/input'      # 备注
        self.choose_all_product = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/table/thead/tr/th[1]/div/label/span/input'
        self.ensure_button = '/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]/span'   # 确定按钮
        self.return_button = '//*[@id="userManage"]/div/div[1]/div/div[1]/button/span'      # 返回按钮


class Home_Big_Wheel_Sow_path(object):
    u"""首页大轮播菜单元素地址"""
    def __init__(self):
        self.Prompt_Message = 'html/body/div[7]/div/div/div[1]/div/span'        # 提示
        self.add_button = '//*[@id="EvaluateManage"]/div/div[1]/div/div[2]/div/button[2]/span'  # 添加按钮
        self.add_title = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[1]/div/div/div/input'     # 标题
        self.Unlinked_type = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[2]/div/div/div/label[1]/span/input'   # 无链接类型
        self.external_links = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[2]/div/div/div/label[2]/span/input'  # 外部链接
        self.external_links_address = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[3]/div/div/div/input'        # 外部链接地址
        self.internal_links = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[2]/div/div/div/label[3]/span/input'  # 内部链接
        self.internal_links_activity = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[3]/div/div/div/label[1]/span/input' # 内部链接-活动详情
        self.choose_activity_button = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[8]/div/div/button/span'      # 选择活动按钮
        self.choose_activity_first = '/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr'  # 选择第一个活动
        self.choose_activity_ensure = '/html/body/div[4]/div[2]/div/div/div[3]/div/button/span'  # 选择活动页面确定按钮
        self.internal_links_product_list = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[3]/div/div/div/label[2]/span/input' # 内部链接-商品列表
        self.links_product_list = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[8]/div/div/div/div[1]/div[2]'    # 商品分类
        self.one_level_product = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[8]/div/div/div/div[2]/div/span/ul/li[%s]' # 分类
        self.two_level_product = "/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[8]/div/div/div/div[2]/div/span/span/ul/li[%s]" # 分类下二级分类
        self.internal_links_product_details = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[3]/div/div/div/label[3]/span/input' # 内部链接-商品详情
        self.links_product_details = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[8]/div/div/button/span'   # 选择商品
        self.choose_product = '/html/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[%s]'    # 选择商品详情
        self.choose_product_ensure = '/html/body/div[5]/div[2]/div/div/div[3]/div/button/span'     # 选择商品详情确定按钮
        self.show_picture = './html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[4]/div/div/div/div/div/input' # 展示图片
        self.upload_picture_succeed = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[4]/div/div/div/div[1]/img'   # 上传成功第一张
        self.rank = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[5]/div/div/div/input'  # 排序
        self.explain = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[6]/div/div/div/input'   # 说明
        self.status = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[7]/div/div/div/div[1]/div/span'  # 状态
        self.start_status = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[7]/div/div/div/div[2]/ul[2]/li[1]' # 1启用
        self.stop_status = '/html/body/div[3]/div[2]/div/div/div[1]/div[2]/form/div/div[7]/div/div/div/div[2]/ul[2]/li[2]'  # 2停用
        self.add_ensure = '/html/body/div[3]/div[2]/div/div/div[2]/div/button[2]/span'  # 添加确定按钮
        self.add_cancel = '/html/body/div[3]/div[2]/div/div/div[2]/div/button[1]/span'  # 添加取消按钮
        self.close_menu = ".//*[@id='app']/div/div[2]/div/div[2]/div[1]/div/div/div/div/a[3]/span[2]/i"  # 关闭菜单
        self.select_list = '//*[@id="EvaluateManage"]/div/div[1]/div/div[3]/div/div/div[2]/table/tbody/tr[%s]/td[1]/div/label/span/input'   # 选择列表项
        self.select_all = ".//*[@id='EvaluateManage']/div/div[1]/div/div[3]/div/div/div[1]/table/thead/tr/th[1]/div/label/span/input" # 选择全部列表项
        self.delete_button = ".//*[@id='EvaluateManage']/div/div[1]/div/div[2]/div/button[1]"   # 选择列表项
        self.delete_ensure = 'html/body/div[6]/div[2]/div/div/div[3]/div/button[2]'  # 删除确定按钮


class Home_Tag_Path(object):
    u"""首页标签-菜单元素地址"""
    def __init__(self):
        self.Prompt_Message = 'html/body/div[2]/div/div/div[1]/div/span'        # 提示
        self.query_tag_name = ".//*[@id='userManage']/div/div/div/form/div/div[1]/div/input"    # 标签名称
        self.query_tag_name_button = ".//*[@id='userManage']/div/div/div/form/div/div[1]/button"    # 标签查询
        self.add_tag_button = ".//*[@id='userManage']/div/div/div/form/div/div[2]/button[2]"    # 添加标签按钮
        self.delete_button = ".//*[@id='userManage']/div/div/div/form/div/div[2]/button[1]"     # 删除标签按钮
        self.tag_name = ".//*[@id='userManage']/div/div/div/form/div[1]/div[1]/div/input"       # 标签名称
        self.tag_sort = '//*[@id="userManage"]/div/div/div/form/div[1]/div[2]/div/div[2]/input' # 标签排序
        self.tag_status = ".//*[@id='userManage']/div/div/div/form/div[1]/div[3]/div/div[1]/div/span"   # 是否启用（默认启用）
        self.status = ".//*[@id='userManage']/div/div/div/form/div[1]/div[3]/div/div[2]/ul[2]/li[%s]"   # 启用状态
        self.tag_type = ".//*[@id='userManage']/div/div/div/form/div[1]/div[4]/div/div[1]/div/span"     # 标签类型
        self.type = ".//*[@id='userManage']/div/div/div/form/div[1]/div[4]/div/div[2]/ul[2]/li[%s]"      # 1.普通类型 2.ATM
        self.tag_photo = '//*[@id="userManage"]/div/div/div/form/div[1]/div[6]/div/div/div/div/div/input'   # 标签图片
        self.update_photo = '//*[@id="userManage"]/div/div/div/form/div[1]/div[6]/div/div/div/div[1]/img'   # 图片上传成功
        self.save_button = ".//*[@id='userManage']/div/div/div/form/div[1]/div[5]/button"               # 保存按钮
        self.add_product = ".//*[@id='userManage']/div/div/div/form/div[2]/div/button[2]"       # 添加商品
        self.delete_product = ".//*[@id='userManage']/div/div/div/form/div[2]/div/button[1]"    # 删除商品
        self.delete_ensure = "//div[2]/div/div/div[3]/div/button[2]"             # 确定删除
        self.delete_cancel = "//div[2]/div/div/div[3]/div/button[1]"              # 取消删除
        self.choose_product = ".//*[@id='userManage']/div/div/div/div[2]/div/div/div[%s]/table/thead/tr/th[1]/div/label/span/input"  # 1.全部商品 2.第一件商品
        self.query_product_name = ".//*[@id='userManage']/div/div/div/form/div/div[1]/div/input"    # 查询商品名称
        self.query_product_name_button = '//*[@id="userManage"]/div/div/div/form/div/div[1]/button/span'         # 查询按钮
        self.add_product_button = ".//*[@id='userManage']/div/div/div/form/div/div[2]/button"       # 添加商品按钮
        self.get_back = ".//*[@id='userManage']/div/div/div/div[1]/button"  # 返回按钮
        self.close_menu = '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div/div/a[3]/span[2]/i'  # 关闭菜单


class Activity(object):
    u"""活动-菜单元素地址"""
    def __init__(self):
        self.add_activity = '//*[@id="userManage"]/div/div/div/form/div/div[3]/div/div/button/span'  # 活动添加按钮
        self.promotion_subject = '//*[@id="userManage"]/div/div/div/div[2]/form/div[1]/div[1]/div/div/div/input'# 活动促销主题
        self.promotion_time = '//*[@id="userManage"]/div/div/div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/div/input' # 促销时间
        self.promotion_photo = '//*[@id="userManage"]/div/div/div/div[2]/form/div[2]/div/div/div/div/div/div/input' # 活动首图
        self.activity_type = '//*[@id="userManage"]/div/div/div/div[2]/form/div[3]/div[1]/div/div[2]/div/div[1]/label[%s]/span[1]/input'   # 1.满减 2.满折
        self.type_piece = '//*[@id="userManage"]/div/div/div/div[2]/form/div[3]/div[1]/div/div[2]/div/div[2]/div/p/div[1]/div[2]/input'    # 件数
        self.type_money = '//*[@id="userManage"]/div/div/div/div[2]/form/div[3]/div[1]/div/div[2]/div/div[2]/div/p/div[2]/div[2]/input'    # 减价或折扣
        self.apply_product = '//*[@id="userManage"]/div/div/div/div[2]/form/div[4]/div[1]/div[1]/div/label[%s]/span[1]/input'   # 使用商品：1.全部 2.指定商品
        self.discount_coupon_together = '//*[@id="userManage"]/div/div/div/div[2]/form/div[4]/div[1]/div[2]/div/label[%s]/span[1]/input'    # 优惠券是否同时使用：1.是 2.否
        self.add_product = '//*[@id="userManage"]/div/div/div/div[2]/div[1]/div[2]/button/span'     # 添加商品
        self.select_all_product = '/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/table/thead/tr/th[1]/div/label/span/input' # 选择1:全部商品
        self.select_product =  '/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div[%s]/table/tbody/tr/td[1]/div/label/span/input' #     2.指定商品
        self.query_product_name = '/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/input'  # 输入商品名称
        self.query_product_name_button = '/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/button'   # 商品名称查询
        self.product_cancel = '/html/body/div[3]/div[2]/div/div/div[3]/div/button[1]/span'  # 取消按钮
        self.product_ensure = '/html/body/div[3]/div[2]/div/div/div[3]/div/button[2]/span'  # 确定按钮
        self.activity_cancel = '//*[@id="userManage"]/div/div/div/div[2]/div[2]/div/div[2]/button[1]/span'  # 活动取消按钮
        self.activity_ensure = '//*[@id="userManage"]/div/div/div/div[2]/div[2]/div/div[2]/button[2]/span'  # 活动保存按钮
        self.query_activity_status = '//*[@id="userManage"]/div/div/div/form/div/div[1]/div/div[1]/div/div[1]/div/span' # 查询活动状态
        self.query_activity_status_list = '//*[@id="userManage"]/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/ul[2]/li'# 查询活动状态列表
        self.query_activity_type = '//*[@id="userManage"]/div/div/div/form/div/div[1]/div/div[2]/div/div[1]/div/span'   # 查询活动类型
        self.query_activity_type_list = '//*[@id="userManage"]/div/div/div/form/div/div[1]/div/div[2]/div/div[2]/ul[2]' # 查询活动类型列表
        self.query_activity_name = '//*[@id="userManage"]/div/div/div/form/div/div[2]/div[1]/div/input'     # 查询活动名称

