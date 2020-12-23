# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : wangyufeng
# @Remark: 已发邮件模块封装
import time
import unittest
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_email.alreadyEmail_locator import alreadyEmailLocator as adel
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class alreadyEmailPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '电子邮件')
        # 点击彩信产品
        MenuUtils(self.driver).menu_tab('li', '发送管理')
        time.sleep(2)
        MenuUtils(self.driver).menu_tab('li', '已发邮件')
        self.driver.implicitly_wait(4)
        comm_frame(self.driver).Frame('mainFrame_154')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data):
        temp = True
        self.click_element(data, "已发邮件-直接点击按扭")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(adel.alreadyEmail_message, "页面顶部提示信息")
        # print(overall_message)
        print(message)
        if message == '请选择一项记录，然后再操作！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False
        return temp

    # 已发邮件-预览
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
            # 直接点击
            temp = self.func_case_0(adel.alreadyEmail_preview)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 已发邮件-重新发送
    def func_alterSend(self, case):
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
            temp = self.func_case_0(adel.alreadyEmail_alterSend)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 模板报备中心——软退一键重发
    def func_keyResend(self, case):
        """
        case=0: 软退一键重发取消
        case=1: 软退一键重发保存
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            self.click_element(adel.alreadyEmail_keyResend, "已发邮件——软退一键重发")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            alter = self.get_element_text(adel.alreadyEmail_alter, "已发邮件——软退一键重发提示语")
            print(alter)
            time.sleep(2)
            if alter in '显示为软退的邮址是已尝试多次发送失败的邮址，'+"\n"+'您确定重新发送？':
                pass
            else:
                print('导出提示语不正确')
                temp = False
            self.driver.implicitly_wait(2)
            self.click_element(adel.alreadyEmail_keyResend_close, "已发邮件——软退一键重发-关闭")
        elif case == 1:
            pass
        return temp

    # 已发邮件——导出
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
        count = self.get_element_text(adel.alreadyEmail_count, "已发邮件——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                self.click_element(adel.alreadyEmail_derive, "已发邮件——导出")
                self.driver.implicitly_wait(2)
                self.driver.switch_to.default_content()  # 释放iframe
                alter = self.get_element_text(adel.alreadyEmail_alter, "已发邮件——导出提示语")
                if alter == '您已成功创建导出任务，请到首页-导入导出-导出任务列表下载':
                    pass
                else:
                    print('导出提示语不正确')
                    temp = False
                self.driver.implicitly_wait(2)
                self.click_element(adel.alreadyEmail_close, "已发邮件——导出-关闭")
            elif case == 1:
                pass
        elif count == 0:
            self.click_element(adel.alreadyEmail_derive, "已发邮件——导出")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(adel.alreadyEmail_message, "已发邮件——页面顶部提示语")
            if message == '当前无可导出的记录！':
                pass
            else:
                print('页面顶部提示语不正确')
                temp = False
        return temp

