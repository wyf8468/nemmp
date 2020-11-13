# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 发送普通彩信模块疯转
import time
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_mms.send_generalMms_locator import SendMmsLocator


class SendMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    def func_basic(self, data, value, time_timeing, valueOne):
        # 选择菜单到发送普通彩信
        MenuUtils(self.driver).menu_tab('li', '彩信')
        MenuUtils(self.driver).menu_tab('li', '发送普通彩信')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_43')  # 获取iframe
        # 输入收件号码
        self.input_text(SendMmsLocator.mms_phone, "发送普通彩信_收件号码", data)
        self.click_element(SendMmsLocator.mms_extractPhone, "发送普通彩信_提取号码")
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        # 关闭提取号码弹窗
        self.click_element(SendMmsLocator.mms_close, "发送普通彩信_关闭弹窗")
        comm_frame(self.driver).Frame('mainFrame_43')  # 获取iframe
        # 选择彩信产品
        self.click_element(SendMmsLocator.mms_select, "发送普通彩信_选择彩信产品")
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_goChoseMmsProduct')  # 获取iframe
        self.click_element(SendMmsLocator.mms_product, "发送普通彩信_勾选彩信产品")
        self.click_element(SendMmsLocator.mms_affirm, "发送普通彩信_确认选择")
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_43')  # 获取iframe
        if value == '立即发送':
            self.click_element(SendMmsLocator.mms_promptly, "发送普通彩信_立即发送")
        # 定时发送
        else:
            self.click_element(SendMmsLocator.mms_timeing, "发送普通彩信_定时发送")
            # 取消readonly属性变为可输入
            js = 'document.getElementById("timingTime").removeAttribute("readonly")'
            self.driver.execute_script(js)
            # 输入定时时间
            self.input_text(SendMmsLocator.time_alarm, "发送普通短信_定时时间", time_timeing)

        self.click_element(SendMmsLocator.mms_submit, "发送普通彩信_提交发送")
        self.driver.switch_to.default_content()  # 释放iframe
        if valueOne == '确认发送':
            self.click_element(SendMmsLocator.mms_send, "发送普通彩信_确认")
        else:
            self.click_element(SendMmsLocator.mms_cancel, "发送普通彩信_取消发送")
        return time_timeing

    # 返回短信审核箱需要验证的列
    def func_checkResults(self, nature):
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_45', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(2)
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature)
        return msg_checkTrOne

    # 结果验证（短信审核箱、已发短信）
    def func_results(self, nature1, textOne, redirect, iframe1, nature2,  textTwo):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_45', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(20)
        self.click_element(SendMmsLocator.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        if msg_dispose.text == '处理成功':
            msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature1)
            # 判断审核状态是否与预期一致
            if msg_checkTrOne.text == textOne:
                self.driver.switch_to.default_content()  # 释放iframe
                time.sleep(2)
                MenuUtils(self.driver).menu_tab('li', redirect)
                time.sleep(2)
                comm_frame(self.driver).Frame(iframe1)
                # 连接数据库循环判断已发短信是否有对应id
                Arr = connectMysql(self.driver).connect_mysql('192.168.0.155', 'nemmp_common', "SELECT * FROM `mms_task_contact`",
                                                          int(getDataId), 0)
                if len(Arr) > 0:
                    for id in Arr:
                        # 通过dataid属性定位元素
                        msg_alreadyTr = self.driver.find_element_by_css_selector('[dataid="' + str(id) + '"]')
                        # 获取属性为'sendStatus'的元素
                        msg_text = getProperty(self.driver).get_pro(msg_alreadyTr, nature2)
                        msg_check = getProperty(self.driver).get_pro(msg_alreadyTr, 'statusCodeEn')
                        # 判断发送状态与预期是否相符
                        if msg_check.text == '余额不足':
                            print(msg_check.text)
                            break
                        if textTwo != msg_text.text:
                            print(msg_alreadyTr.text)
                            print('状态代码：' +msg_text.text)
                            temp = False
                            break
                else:
                    print('找不到元素')
                    temp = False
            else:
                print(msg_checkTrOne.text)
                temp = False
        else:
            print(msg_dispose.text)
            temp = False
        return temp




