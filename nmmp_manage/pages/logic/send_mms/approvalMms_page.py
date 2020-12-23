# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16
# @Author  : wangyufeng
# @Remark: 彩信审核箱模块封装
import time
import unittest

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_mms.approvalMms_locator import approvalMmsLocator as ammsl
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class productsMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '彩信')
        # 点击彩信产品
        MenuUtils(self.driver).menu_tab('li', '我的彩信')
        MenuUtils(self.driver).menu_tab('li', '平台彩信审核箱')
        self.driver.implicitly_wait(4)
        comm_frame(self.driver).Frame('mainFrame_45')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data):
        # 直接点击取消
        self.click_element(data, "平台审核箱-直接点击按钮")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(ammsl.approvalMms_message, "页面顶部提示信息")
        # print(overall_message)
        if message == '请选择一项记录，然后再操作！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False

    # 平台彩信审核箱——取消
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
        if case == 0:
            # 直接点击取消
            self.func_case_0(ammsl.approvalMms_cancel)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 平台审核箱——修改重发
    def func_againSend(self, case):
        """
        case=0:直接点击修改重发
        case=1：选择两条记录，点击修改重发；
        case=2：选择一条审核状态为审核通过的记录，点击修改重发；
        case=3：选择一条审核状态为入库通过的记录，点击修改重发；
        case=4：选择一条审核状态为未审核的记录，点击修改重发；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击修改重发
            self.func_case_0(ammsl.approvalMms_againSend)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 平台彩信审核箱——号码明细
    def func_detail(self, case):
        """
        case=0: 直接点击号码明细
        case=1：选择两条记录，点击号码明细；
        case=2：选择一条记录，点击号码明细；
        :param case:
        :return:
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击号码明细
            self.func_case_0(ammsl.approvalMms_detail)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 平台彩信审核箱——彩信预览
    def func_preview(self, case):
        """
        case=0: 直接点击号码明细
        case=1：选择两条记录，点击号码明细；
        case=2：选择一条记录，点击号码明细；
        :param case:
        :return:
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击彩信预览
            self.func_case_0(ammsl.approvalMms_preview)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 平台彩信审核箱——导出
    def func_derive(self, case):
        """
        case=0: 导出-全部导出
        case=1：导出-具体导出；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        count = self.get_element_text(ammsl.approvalMms_count, "平台彩信审核箱——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                self.click_element(ammsl.approvalMms_derive, "平台彩信审核箱——导出")
                self.driver.implicitly_wait(2)
                self.driver.switch_to.default_content()  # 释放iframe
                alter = self.get_element_text(ammsl.approvalMms_alter, "平台彩信审核箱——导出提示语")
                if alter == '您已成功创建导出任务，请到首页-导入导出-导出任务列表下载':
                    pass
                else:
                    print('导出提示语不正确')
                    temp = False
                self.driver.implicitly_wait(2)
                self.click_element(ammsl.approvalMms_close, "平台彩信审核箱——导出-关闭")
            elif case == 1:
                pass
        elif count == 0:
            self.click_element(ammsl.approvalMms_derive, "平台彩信审核箱——导出")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(ammsl.approvalMms_message, "平台彩信审核箱——页面顶部提示语")
            if message == '当前无可导出的记录！':
                pass
            else:
                print('页面顶部提示语不正确')
                temp = False
        return temp