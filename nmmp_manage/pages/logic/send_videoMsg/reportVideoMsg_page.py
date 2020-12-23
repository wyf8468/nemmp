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
from nmmp_manage.pages.element.send_videoMsg.reportVideoMsg_locator import reportVideoMsgLocator as rvml
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class reportVideoMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver
        overall_message = '请选择一项记录，然后再操作！'

    def func_comm(self):
        MenuUtils(self.driver).menu_tab('li', '视频短信')
        # 点击彩信产品
        MenuUtils(self.driver).menu_tab('li', '我的视频短信')
        MenuUtils(self.driver).menu_tab('li', '模板报备中心')
        self.driver.implicitly_wait(4)
        comm_frame(self.driver).Frame('mainFrame_1884')  # 获取iframe
        self.driver.implicitly_wait(2)

    def func_case_0(self, data, data1):
        temp = True
        self.click_element(data, "模板报备中心-直接点击按扭")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()  # 释放iframe
        message = self.get_element_text(rvml.reportVideo_message, "页面顶部提示信息")
        # print(overall_message)
        print(message)
        if message == data1:
            pass
        else:
            print('页面顶部提示语不正确')
            temp = False
        return temp

    # 模板报备中心——编辑
    def func_compile(self, case):
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
            temp = self.func_case_0(rvml.reportVideo_compile, '请选择一条记录操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 模板报备中心——删除
    def func_delete(self, case):
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
            # 直接点击删除
            temp = self.func_case_0(rvml.reportVideo_delete, '请至少选择一条记录进行操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        return temp

    # 模板报备中心——取消
    def func_cancel(self, case):
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
            temp = self.func_case_0(rvml.reportVideo_cancel, '请选择一条记录操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        return temp

    # 模板报备中心——提交审核
    def func_audit(self, case):
        """
        case=0:直接点击
        case=1：选择两条记录；
        case=2：选择一条记录审核通过的记录；
        case=3：选择一条记录未提交的记录；
        case=4：选择一条记录提交中的记录；
        case=5：选择一条记录驳回的记录；
        :param case:
        :return: temp
        """
        temp = True
        self.func_comm()
        time.sleep(2)
        if case == 0:
            # 直接点击取消
            temp = self.func_case_0(rvml.reportVideo_audit, '请至少选择一条记录进行操作！')
        elif case == 1:
            pass
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        elif case == 5:
            pass
        return temp

    # 模板报备中心——导出
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
        count = self.get_element_text(rvml.reportVideo_count, "模板报备中心——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        if count > 0:
            if case == 0:
                self.click_element(rvml.reportVideo_derive, "模板报备中心——导出")
                self.driver.implicitly_wait(2)
                self.driver.switch_to.default_content()  # 释放iframe
                alter = self.get_element_text(rvml.reportVideo_alter, "模板报备中心——导出提示语")
                if alter == '您已成功创建导出任务，请到首页-导入导出-导出任务列表下载':
                    pass
                else:
                    print('导出提示语不正确')
                    temp = False
                self.driver.implicitly_wait(2)
                self.click_element(rvml.reportVideo_close, "模板报备中心——导出-关闭")
            elif case == 1:
                pass
        elif count == 0:
            self.click_element(rvml.reportVideo_derive, "模板报备中心——导出")
            self.driver.implicitly_wait(2)
            self.driver.switch_to.default_content()  # 释放iframe
            message = self.get_element_text(rvml.reportVideo_message, "模板报备中心——页面顶部提示语")
            if message == '当前无可导出的记录！':
                pass
            else:
                print('页面顶部提示语不正确')
                temp = False
        return temp

