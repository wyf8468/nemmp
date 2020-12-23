# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : wangyufeng
# @Remark: 邮件审核箱模块封装
import time
import unittest
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_email.approvalEmail_locator import approvalEmailLocator as ael
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class approvalEmailPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '电子邮件')
        # 点击彩信产品
        MenuUtils(self.driver).menu_tab('li', '发送管理')
        time.sleep(2)
        MenuUtils(self.driver).menu_tab('li', '邮件审核箱')
        self.driver.implicitly_wait(4)
        comm_frame(self.driver).Frame('mainFrame_106')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data, data1):
        temp = True
        self.click_element(data, "邮件审核箱-直接点击按扭")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(ael.approvalEmail_message, "页面顶部提示信息")
        # print(overall_message)
        print(message)
        if message == data1:
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False
        return temp

    # 邮件审核箱-修改重发
    def func_alterRetry(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条审核状态为未审核的记录；
        case=3：选择一条审核状态为审核通过的记录；
        case=4：选择一条审核状态为入库成功的记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            # 直接点击
            temp = self.func_case_0(ael.approvalEmail_alterRetry, '请选择一项记录，然后再操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 邮件审核箱-取消
    def func_cancel(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条审核状态为未审核的记录；
        case=3：选择一条审核状态为审核通过的记录；
        case=4：选择一条审核状态为入库成功的记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            # 直接点击
            temp = self.func_case_0(ael.approvalEmail_cancel, '请选择一项记录，然后再操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 已发视频短信——邮址明细
    def func_Detail(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            # 直接点击
            temp = self.func_case_0(ael.approvalEmail_Detail, '请选择一条记录进行操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 已发视频短信——附件下载
    def func_upDown(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            # 直接点击
            temp = self.func_case_0(ael.approvalEmail_upDown, '请选择一条记录，然后再操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 已发视频短信——预览
    def func_preview(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            # 直接点击编辑
            temp = self.func_case_0(ael.approvalEmail_preview, '请选择一条记录进行操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 邮件审核箱——导出
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
        count = self.get_element_text(ael.approvalEmail_count, "邮件审核箱——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                self.click_element(ael.approvalEmail_derive, "邮件审核箱——导出")
                self.driver.implicitly_wait(2)
                self.driver.switch_to.default_content()  # 释放iframe
                alter = self.get_element_text(ael.approvalEmail_alter, "邮件审核箱——导出提示语")
                if alter == '您已成功创建导出任务，请到首页-导入导出-导出任务列表下载':
                    pass
                else:
                    print('导出提示语不正确')
                    temp = False
                self.driver.implicitly_wait(2)
                self.click_element(ael.approvalEmail_close, "邮件审核箱——导出-关闭")
            elif case == 1:
                pass
        elif count == 0:
            self.click_element(ael.approvalEmail_derive, "邮件审核箱——导出")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(ael.approvalEmail_message, "邮件审核箱——页面顶部提示语")
            if message == '当前无可导出的记录！':
                pass
            else:
                print('页面顶部提示语不正确')
                temp = False
        return temp

