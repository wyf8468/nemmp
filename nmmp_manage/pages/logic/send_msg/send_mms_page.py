# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 发送普通彩信
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_mms_locator import SendMmsLocator


class SendMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送彩信
    def send_Mms(self, phone):
        self.input_text(SendMmsLocator.mms_phone, "发送普通彩信_收件号码", phone)
        self.click_element(SendMmsLocator.mms_extractPhone, "发送普通彩信_提取号码")


    # 关闭弹窗
    def send_close(self):
        self.click_element(SendMmsLocator.mms_close, "发送普通彩信_关闭弹窗")

    # 选择产品
    def send_select(self):
        self.click_element(SendMmsLocator.mms_select, "发送普通彩信_选择彩信产品")

    # 选择彩信产品
    def send_product(self):
        self.click_element(SendMmsLocator.mms_product, "发送普通彩信_勾选彩信产品")
        self.click_element(SendMmsLocator.mms_affirm, "发送普通彩信_确认选择")

    # 发送
    def send_submit(self):
        self.click_element(SendMmsLocator.mms_promptly, "发送普通彩信_立即发送")
        self.click_element(SendMmsLocator.mms_submit, "发送普通彩信_提交发送")

    # 确认发送
    def send_confirm(self):
        self.click_element(SendMmsLocator.mms_send, "发送普通彩信_确认")
