# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17
# @Author  : wangyufeng
# @Remark: 定时彩信模块封装
import time
import unittest

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_mms.timingMms_locator import timingMmsLocator as tmmsl
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class productsMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '彩信')
        # 点击彩信产品
        MenuUtils(self.driver).menu_tab('li', '我的彩信')
        MenuUtils(self.driver).menu_tab('li', '定时彩信')
        self.driver.implicitly_wait(4)
        comm_frame(self.driver).Frame('mainFrame_46')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data):
        self.click_element(data, "平台审核箱-直接点击按钮")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(tmmsl.timingMms_message, "页面顶部提示信息")
        # print(overall_message)
        if message == '请选择一项记录，然后再操作！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False

    # 定时彩信——取消
    def func_cancel(self, case):
        """
        case=0:直接点击取消
        case=1：选择两条记录，点击取消；
        case=2：选择一条审核状态为审核通过的记录，点击取消；
        case=3：选择一条审核状态为入库通过的记录，点击取消；
        case=4：选择一条审核状态为未审核的记录，点击取消；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        count = self.get_element_text(tmmsl.timingMms_count, "定时彩信——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                # 直接点击取消
                self.func_case_0(tmmsl.timingMms_cancel)
            elif case == 1:
                pass
            elif case == 2:
                pass
            elif case == 3:
                pass
            elif case == 4:
                pass
        else:
            print('当前列表无记录')
            temp = False
        return temp

    # 定时彩信——预览
    def func_preview(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条审核状态为审核通过的记录；
        case=3：选择一条审核状态为入库通过的记录；
        case=4：选择一条审核状态为未审核的记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        count = self.get_element_text(tmmsl.timingMms_count, "定时彩信——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                # 直接点击取消
                self.func_case_0(tmmsl.timingMms_preview)
            elif case == 1:
                pass
            elif case == 2:
                pass
            elif case == 3:
                pass
            elif case == 4:
                pass
        else:
            print('当前列表无记录')
            temp = False
        return temp

