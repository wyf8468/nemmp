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
from nmmp_manage.pages.element.send_videoMsg.approvaVideoMsg_locator import alreadyVideoMsgLocator as avml
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class alreadyVideoMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '视频短信')
        # 点击彩信产品
        MenuUtils(self.driver).menu_tab('li', '我的视频短信')
        MenuUtils(self.driver).menu_tab('li', '视频短信审核箱')
        self.driver.implicitly_wait(4)
        comm_frame(self.driver).Frame('mainFrame_1878')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data):
        self.click_element(data, "视频短信审核箱-直接点击按扭")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(avml.alreadyVideo_message, "页面顶部提示信息")
        # print(overall_message)
        if message == '请选择一项记录，然后再操作！':
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False

    # 视频短信审核箱——预览
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
            # 直接点击取消
            self.func_case_0(avml.alreadyVideo_preview)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 视频短信审核箱——号码明细
    def func_phoneDetail(self, case):
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
            # 直接点击取消
            self.func_case_0(avml.alreadyVideo_phoneDetail)
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 视频短信审核箱——取消发送
    def func_cancelSend(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条记录审核通过的记录；
        case=3：选择一条记录入库成功的记录；
        case=4：选择一条记录未审核的记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            # 直接点击取消
            self.func_case_0(avml.alreadyVideo_cancel)
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 视频短信审核箱——导出
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
        count = self.get_element_text(avml.alreadyVideo_count, "已发彩信——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                self.click_element(avml.alreadyVideo_derive, "已发彩信——导出")
                self.driver.implicitly_wait(2)
                self.driver.switch_to.default_content()  # 释放iframe
                alter = self.get_element_text(avml.alreadyVideo_alter, "已发彩信——导出提示语")
                if alter == '您已成功创建导出任务，请到首页-导入导出-导出任务列表下载':
                    pass
                else:
                    print('导出提示语不正确')
                    temp = False
                self.driver.implicitly_wait(2)
                self.click_element(avml.alreadyVideo_close, "已发彩信——导出-关闭")
            elif case == 1:
                pass
        elif count == 0:
            self.click_element(avml.alreadyVideo_derive, "已发彩信——导出")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(avml.alreadyVideo_message, "已发彩信——页面顶部提示语")
            if message == '当前无可导出的记录！':
                pass
            else:
                print('页面顶部提示语不正确')
                temp = False
        return temp

