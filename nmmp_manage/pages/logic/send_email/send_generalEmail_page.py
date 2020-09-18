# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送普通邮件模块封装
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_email.send_generalEmail_locator import SendGemailMsgLocator as sgeml


class SendGemailPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送普通邮件
    def send_receive(self, receive):
        self.input_text(sgeml.gemail_receive, "发送普通邮件_输入收件人", receive)
        self.click_element(sgeml.gemail_extract, "发送普通邮件_提取邮件")

    # 点击关闭弹窗按钮
    def send_extractClose(self):
        self.click_element(sgeml.gemail_extractClose, "发送普通邮件_提取邮件关闭弹窗")

    # 点击选择模板
    def send_select(self):
        self.click_element(sgeml.gemail_select, "发送普通邮件_选择模板")

    # 点击勾选复选框
    def send_checkbox(self):
        self.click_element(sgeml.gemail_checkbox, "发送普通邮件_勾选复选框")
        self.click_element(sgeml.gemail_checkboxAffirm, "发送普通邮件_勾选复选框确认选择模板")

    # 发送普通邮件，点击测试发送
    def send__senderName(self, senderName, theme):
        self.input_text(sgeml.gemail_senderName, "发送普通邮件_输入收件人名称", senderName)
        self.input_text(sgeml.gemail_theme, "发送普通邮件_输入邮件主题", theme)
        self.click_element(sgeml.gemail_submit, "发送普通邮件_测试发送")

    # 输入发送邮址，确认发送
    def send_mailAddress(self, address):
        self.input_text(sgeml.gemail_mailAddress, "发送普通邮件_输入收件人名称", address)
        self.click_element(sgeml.gemail_send, "发送普通邮件_确认发送")
