# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送生日短信页面模块封装
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_birthdayMsg_locator import SendBirthMsgLocator as sbml


class SendBirthMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 点击导入按钮
    def send_upload(self):
        self.click_element(sbml.birthday_receipt, "发送生日短信_点击导入")

    # 发送生日短信
    def send_birthday_msg(self,  content):
        self.input_text(sbml.birthday_content, "发送生日短信_输入短信内容", content)
        self.click_element(sbml.birthday_days, "发送生日短信_发送时间（天）")

    # 发送时间时
    def send_hour(self):
        self.click_element(sbml.birthday_hour, "发送生日短信_发送时间（时）")

    # 发送时间分
    def send_minute(self):
        self.click_element(sbml.birthday_minute, "发送生日短信_发送时间（分）")

    # 预处理
    def send_dispose(self):
        self.click_element(sbml.birthday_dispose, "发送生日短信_预处理")

    # 弹窗-确认
    def send_affirm(self):
        self.click_element(sbml.birthday_affirm, "发送生日短信_确认")

