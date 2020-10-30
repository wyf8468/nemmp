# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送生日短信页面模块封装
import time

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.fileUpload import UpLoad_File
from nmmp_manage.common.menuUtils import MenuUtils
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

    def func_basic(self, data1, data2, data3, data4, data5):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '直客短信')
        MenuUtils(self.driver).menu_tab('li', '发送生日短信')
        time.sleep(1)
        comm_frame(self.driver).Frame('mainFrame_353')  # 获取iframe
        self.send_upload()
        UpLoad_File(data1)
        time.sleep(2)
        self.send_birthday_msg(data2)
        MenuUtils(self.driver).menu_tab('li', data3)
        self.send_hour()
        MenuUtils(self.driver).menu_tab('li', data4)
        self.send_minute()
        MenuUtils(self.driver).menu_tab('li', data5)
        self.send_dispose()
        self.driver.switch_to.default_content()  # 释放iframe


