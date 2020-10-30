# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送普通邮件模块封装
import time
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_email.send_generalEmail_locator import SendGemailMsgLocator as sgeml
from nmmp_manage.common.comm_readonly import comm_readonly


class SendGemailPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    def func_basic(self, data1, data2, data3, value, time_timeing, data4, valueOne, valueTwo):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '电子邮件')
        MenuUtils(self.driver).menu_tab('li', '发送管理')
        MenuUtils(self.driver).menu_tab('li', '发送普通邮件')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_105')  # 获取iframe
        self.input_text(sgeml.gemail_receive, "发送普通邮件_输入收件人", data1)
        self.click_element(sgeml.gemail_extract, "发送普通邮件_提取邮件")
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        self.click_element(sgeml.gemail_extractClose, "发送普通邮件_提取邮件关闭弹窗")
        comm_frame(self.driver).Frame('mainFrame_105')  # 获取iframe
        self.click_element(sgeml.gemail_select, "发送普通邮件_选择模板")
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_goTemplateList')  # 获取iframe
        time.sleep(2)
        self.click_element(sgeml.gemail_checkbox, "发送普通邮件_勾选复选框")
        self.click_element(sgeml.gemail_checkboxAffirm, "发送普通邮件_勾选复选框确认选择模板")
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_105')  # 获取iframe
        self.input_text(sgeml.gemail_senderName, "发送普通邮件_输入收件人名称", data2)
        # 取消readonly属性变为可输入
        comm_readonly(self.driver).readonly('sendMailAddress')
        # 输入发件人域名
        time.sleep(2)
        self.input_text(sgeml.gemail_domain, "发送普通短信_定时时间", 'marketing@send.szaisiou.com')
        self.input_text(sgeml.gemail_theme, "发送普通邮件_输入邮件主题", data3)
        if value == '立即发送':
            self.click_element(sgeml.gemail_now, "发送普通邮件_立即发送")
        elif value == '定时发送':
            self.click_element(sgeml.gemail_timeing, "发送普通邮件_定时发送")
            comm_readonly(self.driver).readonly('timingTime')
            # 输入发件人域名
            time.sleep(2)
            self.input_text(sgeml.time_timeing, "发送普通短信_定时时间", time_timeing)
        if valueOne == '测试发送':
            self.click_element(sgeml.gemail_submit, "发送普通邮件_测试发送")
            time.sleep(2)
            self.driver.switch_to.default_content()  # 释放iframe
            self.input_text(sgeml.gemail_mailAddress, "发送普通邮件_输入收件人名称", data4)
            if valueTwo == '确认发送':
                self.click_element(sgeml.gemail_send, "发送普通邮件_确认发送")
                time.sleep(2)
                self.click_element(sgeml.msg_confirm, "发送普通邮件_确定")
            elif valueTwo == '取消发送':
                self.click_element(sgeml.gemail_cancel, "发送普通邮件_取消发送")
        elif valueOne == '提交发送':
            self.click_element(sgeml.gemail_commit, "发送普通邮件_提交发送")
            self.driver.switch_to.default_content()  # 释放iframe
            if valueTwo == '确认发送':
                time.sleep(2)
                self.click_element(sgeml.gemail_extractClose, "发送普通邮件_确认发送_关闭")
                time.sleep(2)

    # 结果验证（短信审核箱、已发短信）
    def func_results(self, nature1, textOne, redirect, iframe1, nature2, nature3, textTwo):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_106', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(18)
        # wait = WebDriverWait(driver, 20)
        self.click_element(sgeml.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        if msg_dispose.text == "处理完成":
            msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature1)
            # 判断审核状态是否与预期一致
            if msg_checkTrOne.text == textOne:
                self.driver.switch_to.default_content()  # 释放iframe
                time.sleep(2)
                MenuUtils(self.driver).menu_tab('li', redirect)
                time.sleep(2)
                comm_frame(self.driver).Frame(iframe1)
                time.sleep(5)
                self.click_element(sgeml.video_refresh, "短信审核箱_刷新")
                # 连接数据库循环判断已发短信是否有对应id
                Arr = connectMysql(self.driver).connect_mysql('192.168.0.155', 'nemmp_common', "SELECT * FROM `mail_task_contact`",
                                                          int(getDataId), 0)
                if len(Arr) > 0:
                    for id in Arr:
                        # 通过dataid属性定位元素
                        msg_alreadyTr = self.driver.find_element_by_css_selector('[dataid="' + str(id) + '"]')
                        # 获取属性为'returnMsg'的元素
                        msg_text = getProperty(self.driver).get_pro(msg_alreadyTr, nature2)
                        msg_return = getProperty(self.driver).get_pro(msg_alreadyTr, nature3)
                        # 判断发送状态与预期是否相符
                        if textTwo != msg_text.text:
                            print(msg_alreadyTr.text)
                            print('状态：' +msg_text.text)
                            print('投递详情：' + msg_return.text)
                            temp = False
                            break
                else:
                    print('找不到元素')
                    temp = False
            else:
                print(msg_checkTrOne.text + '不等于入库成功（等待时间12s）')
                temp = False
        else:
            print(msg_dispose.text + '不等于处理完成')
            temp = False
        return temp





