# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2
# @Author  : wangyufeng
# @Remark: 已发短信模块封装
import time

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.alreadyMsg_locator import alreadyMsgLocator as aml
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class approvalMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '直客短信')
        # 点击短信审核箱
        MenuUtils(self.driver).menu_tab('li', '已发短信')
        comm_frame(self.driver).Frame('mainFrame_30')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data):
        self.click_element(data, "已发短信——直接点击按钮")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(aml.already_message, "页面顶部提示信息")
        # print(overall_message)
        if message == '请选择一项记录，然后再操作！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False

    # 已发短信——编辑重发
    def func_editSend(self, case):
        """
        case=0:直接点击编辑重发
        case=1：选择两条记录，点击编辑重发；
        case=2：选择一条审核状态为审核通过的记录，点击编辑重发；
        case=3：选择一条审核状态为入库通过的记录，点击编辑重发；
        case=4：选择一条审核状态为未审核的记录，点击编辑重发；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击编辑重发
            self.func_case_0(aml.already_details)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 已发短信——时间段导出
    def func_timeDerive(self, case):
        """
        case=0: 时间段导出-取消
        case=1：时间段导出-导出；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            self.click_element(aml.already_timeDerive, "已发短信——时间段导出")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            self.click_element(aml.already_timeCancel, "已发短信——时间段导出-取消")
        elif case == 1:
            pass
        return temp

    # 已发短信——导出
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
        count = self.get_element_text(aml.already_count, "已发短信——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                self.click_element(aml.already_derive, "已发短信——时间段导出")
                self.driver.implicitly_wait(2)
                self.driver.switch_to.default_content()  # 释放iframe
                alter = self.get_element_text(aml.already_alter, "已发短信——导出提示语")
                if alter == '您已成功创建导出任务，请到首页-导入导出-导出任务列表下载':
                    pass
                else:
                    print('导出提示语不正确')
                    temp = False
                self.click_element(aml.already_alterClose, "已发短信——导出-关闭")
            elif case == 1:
                pass
        elif count == 0:
            self.click_element(aml.already_derive, "已发短信——时间段导出")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(aml.already_message, "已发短信——页面顶部提示语")
            if message == '当前无可导出的记录！':
                pass
            else:
                print('页面顶部提示语不正确')
                temp = False
        return temp