# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2
# @Author  : wangyufeng
# @Remark: 短信审核箱模块封装
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.approvalMsg_locator import approvalMsgLocator as saml


class approvalMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '直客短信')
        # 点击短信审核箱
        MenuUtils(self.driver).menu_tab('li', '短信审核箱')
        comm_frame(self.driver).Frame('mainFrame_28')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data):
        self.click_element(data, "短信审核箱——直接点击按钮")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(saml.approvalMsg_message, "页面顶部提示信息")
        # print(overall_message)
        if message == '请选择一项记录，然后再操作！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False

    # 短信审核箱——取消
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
            self.func_case_0(saml.approvalMsg_cancel)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 短信审核箱——修改重发
    def func_alterRetry(self, case):
        """
        case=0: 直接点击修改重发
        case=1：选择两条记录，点击修改重发；
        case=2：选择一条审核状态为审核通过的记录，点击修改重发；
        case=3：选择一条审核状态为入库通过的记录，点击修改重发；
        case=4：选择一条审核状态为未审核的记录，点击修改重发；
        :param case:
        :return:
        """
        temp = True
        self.func_comm()
        if case == 0:
            # 直接点击修改重发
            self.func_case_0(saml.approvalMsg_alterRetry)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 短信审核箱——号码明细
    def func_phoneDetail(self, case):
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
            self.func_case_0(saml.approvalMsg_phoneDetail)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 短信审核箱——导出
    def func_derive(self, case):
        """
        case=0: 导出当前页选中的数据
        case=1：导出列表全部数据
        """
        temp = True
        self.func_comm()
        self.click_element(saml.approvalMsg_derive, "短信审核箱——导出数据")
        self.driver.implicitly_wait(2)
        if case == 0:
            self.click_element(saml.approvalMsg_selectDerive, "短信审核箱——导出当前页选中的数据")
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(saml.approvalMsg_message, "页面顶部提示信息")
            if message == '当前页未选中数据，无法导出':
                pass
            else:
                print('导出当前页选中记录功能—提示语不正确')
                temp = False
        elif case == 1:
            self.click_element(saml.approvalMsg_allDerive, "短信审核箱——导出列表全部数据")
            self.driver.switch_to.default_content()  # 释放iframe

        return temp

