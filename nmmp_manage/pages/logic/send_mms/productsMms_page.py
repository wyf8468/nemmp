# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16
# @Author  : wangyufeng
# @Remark: 彩信产品模块封装
import unittest

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_mms.productsMms_locator import productsMmsLocator as pmmsl


class productsMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '彩信')
        # 点击彩信产品
        MenuUtils(self.driver).menu_tab('li', '我的彩信')
        MenuUtils(self.driver).menu_tab('li', '彩信产品')
        self.driver.implicitly_wait(4)
        comm_frame(self.driver).Frame('mainFrame_44')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data):
        # 直接点击products取消
        self.click_element(data, "彩信产品——直接点击按钮")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(pmmsl.productsMms_message, "页面顶部提示信息")
        # print(overall_message)
        if message == '未选择任何项！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False

    @unittest.skip('彩信产品-制作彩信')
    # 彩信产品——制作彩信
    def func_make(self):
        """
        :param:
        :return: temp
        """
        temp = True
        self.func_comm()

    # 彩信产品——修改
    def func_modification(self, case):
        """
        case=0:直接点击修改
        case=1：选择两条记录，点击修改；
        case=2：选择一条记录点击修改；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击修改
            self.func_case_0(pmmsl.productsMms_modification)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 彩信产品——预览
    def func_preview(self, case):
        """
        case=0:直接点击预览
        case=1：选择两条记录，点击预览；
        case=2：选择一条记录点击预览；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击预览
            self.func_case_0(pmmsl.productsMms_preview)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 彩信产品——删除
    def func_delete(self, case):
        """
        case=0:直接点击删除
        case=1：选择两条记录，点击删除；
        case=2：选择一条记录点击删除；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击products取消
            self.click_element(pmmsl.productsMms_delete, "彩信产品——删除")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(pmmsl.productsMms_alter, "弹窗提示语")
            # print(overall_message)
            if message == '一旦删除后，将无法恢复，您确认删除吗？':
                self.click_element(pmmsl.productsMms_sure, "彩信产品——删除-确定")
                message1 = self.get_element_text(pmmsl.productsMms_message, "弹窗提示语")
                if message1 == '未选择任何项！':
                    pass
                else:
                    print('彩信产品删除功能—页面顶部删除提示语错误')
            else:
                print('彩信产品修改功能—弹窗提示语不正确')
                temp = False
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp