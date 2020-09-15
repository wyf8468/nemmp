# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11
# @Author  : wangyufeng
# @Remark: 发送个性短信页面模块封装
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_personalityMsg_locator import SendPersonMsgLocator as sendPerMsg


class SendPerMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送普通短信
    def send_personality_msg(self,  text):
        self.input_text(sendPerMsg.msg_content, "发送个性短信_输入短信内容", text)
        self.click_element(sendPerMsg.pre_processing, "发送个性短信_预处理")
        self.click_element(sendPerMsg.send_ensure, "发送个性短信_发送")
    # 点击导入按钮
    def send_lead(self):
        self.click_element(sendPerMsg.receipt_phone, "发送个性短信_点击导入")
