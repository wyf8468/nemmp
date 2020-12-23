# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  : wangyufeng
# @Remark: 生日短信模块封装
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.birthdayMsg_locator import birthdayMsgLocator as bml


class birthdayMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '直客短信')
        # 点击短信审核箱
        MenuUtils(self.driver).menu_tab('li', '生日短信')
        comm_frame(self.driver).Frame('mainFrame_354')  # 获取iframe
        self.driver.implicitly_wait(4)

    def func_case_0(self, data):
        self.click_element(data, "生日短信——直接点击按钮")
        self.driver.implicitly_wait(4)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(bml.birthday_message, "页面顶部提示信息")
        # print(overall_message)
        if message == '请选择一项记录，然后再操作！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False

    # 生日短信——查看详情
    def func_details(self, case):
        """
        case=0: 直接点击查看详情
        case=1：选择两条记录，点击查看详情；
        case=2：选择一条记录，点击查看详情；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击查看详情
            self.func_case_0(bml.birthday_details)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 生日短信——取消发送
    def func_cancel(self, case):
        """
        case=0: 直接点击取消发送
        case=1：选择两条记录，点击取消发送；
        case=2：选择一条发送状态为未发送的记录，点击取消发送；
        case=3：选择一条发送状态为发送中的记录，点击取消发送；
        case=4：选择一条发送状态为发送完成的记录，点击取消发送；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击取消发送
            self.func_case_0(bml.birthday_cancel)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp