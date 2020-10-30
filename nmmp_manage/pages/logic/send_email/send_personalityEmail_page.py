# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 发送个性邮件模块封装
import time

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_email.send_personalityEmail_locator import SendPemailMsgLocator as speml


class SendPemailPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送个性邮件导入收件人
    def send_receive(self, receive):
        self.input_text(speml.pemail_receive, "发送个性邮件_选择模板", receive)
        self.click_element(speml.pemail_upload, "发送个性邮件_导入")
        self.click_element(speml.pemail_select, "发送个性邮件_选择模板")

    # 点击勾选复选框
    def send_checkbox(self):
        self.click_element(speml.pemail_checkbox, "发送个性邮件_勾选复选框")
        self.click_element(speml.pemail_checkboxAffirm, "发送个性邮件_勾选复选框确认选择模板")

    # 发送普通邮件，点击测试发送
    def send_senderName(self, senderName, theme):
        self.input_text(speml.pemail_senderName, "发送个性邮件_输入收件人名称", senderName)
        self.input_text(speml.pemail_theme, "发送个性邮件_输入邮件主题", theme)
        self.click_element(speml.pemail_submit, "发送个性邮件_提交发送")

    # 输入发送邮址，确认发送
    def send_affirm(self):
        self.click_element(speml.pemail_affirm, "发送个性邮件_确认")

    def func_basic(self, data1, data2, data3):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '电子邮件')
        MenuUtils(self.driver).menu_tab('li', '发送管理')
        MenuUtils(self.driver).menu_tab('li', '发送个性邮件')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_310')  # 获取iframe
        self.send_receive(data1)
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_goTemplateList')  # 获取iframe
        self.send_checkbox()
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_310')  # 获取iframe
        time.sleep(2)
        self.send_senderName(data2, data3)
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe

