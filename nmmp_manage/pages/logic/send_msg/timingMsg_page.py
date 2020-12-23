# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  : wangyufeng
# @Remark: 定时短信模块封装
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.timingMsg_locator import timingMsgLocator as stml


class timingMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '直客短信')
        # 点击短信审核箱
        MenuUtils(self.driver).menu_tab('li', '定时短信')
        comm_frame(self.driver).Frame('mainFrame_29')  # 获取iframe
        self.driver.implicitly_wait(4)

    # 定时短信——取消
    def func_cancel(self, case):
        """
        case=0: 直接点击取消
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
            self.click_element(stml.timing_cancel, "定时短信——取消")
            self.driver.implicitly_wait(4)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(stml.timing_message, "页面顶部提示信息")
            # print(overall_message)
            if message == '请选择一项记录，然后再操作！':
                pass
            else:
                print('取消功能—提示语不正确')
                temp = False
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp