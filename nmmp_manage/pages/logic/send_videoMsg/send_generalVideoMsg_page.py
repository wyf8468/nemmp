# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17
# @Author  : wangyufeng
# @Remark: 发送普通视频短信页面模块封装
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_videoMsg.send_generalVideoMsg_locator import SendVideoMsgLocator as videoMsgLoc


class SendVedioMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送普通短信
    def send_vedio_msg(self,  phone):
        self.input_text(videoMsgLoc.videoMsg_phone, "发送普通视频短信_输入收件号码", phone)
        self.click_element(videoMsgLoc.videoMsg_extract, "发送普通视频短信_提取号码")

    # 点击关闭弹窗
    def send_vedioClose(self):
        self.click_element(videoMsgLoc.videoMsg_close, "发送普通视频短信_点击关闭弹窗")

    # 点击选择视频短信产品
    def send_vedioProduct(self):
        self.click_element(videoMsgLoc.videoMsg_product, "发送普通视频短信_点击选择视频短信产品")

    # 点击选择视频短信产品第一个产品
    def send_vedioCheckbox(self):
        self.click_element(videoMsgLoc.videoMsg_check, "发送普通视频短信_勾选复选框")
        self.click_element(videoMsgLoc.videoMsg_affirm, "发送普通视频短信_确认选择")

    # 点击提交发送
    def send_vedioSubmit(self):
        self.click_element(videoMsgLoc.videoMsg_submit, "发送普通视频短信_提交发送")

    # 点击确定
    def send_vedioConfirm(self):
        self.click_element(videoMsgLoc.videoMsg_confirm, "发送普通视频短信_点击确定")

