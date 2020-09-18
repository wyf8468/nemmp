# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/04
# @Author  : wangyufeng
# @Remark: 发送普通短信页面模块封装
import logging
import time

from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_generalMsg_locator import SendMsgLocator as sendMsg

class SendMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送普通短信
    def send_normal_msg(self, receiptPhone, text):
        self.input_text(sendMsg.receipt_phone, "发送普通短信_输入手机号", receiptPhone)
        self.input_text(sendMsg.msg_content, "发送普通短信_输入短信内容", text)

    # 提交发送
    def send_submit(self):
        self.click_element(sendMsg.send_submit, "发送普通短信_点击提交发送")

    # 获取提交失败提示信息
    def get_errorMsg(self):
        return self.get_element_text(sendMsg.send_error, "提交失败提示！")

    # 获取弹窗提示
    def get_popMsg(self):
        return self.get_element_text(sendMsg.send_hint, "弹窗提示！")
    # 短信计费
    def get_billing(self):
        return self.get_element_text(sendMsg.msg_billing, "短信计费条数")

    # 提取号码总数
    def get_phoneNum(self):
        return self.get_element_text(sendMsg.msg_phoneSum, "提取号码总数")

    # 提取号码错误号码
    def get_errorPhone(self):
        return self.get_element_text(sendMsg.msg_errorPhone, "提取号码错误号码")

    # 提取号码重复号码
    def get_repetitionPhone(self):
        return self.get_element_text(sendMsg.msg_repetitionPhone, "提取号码重复号码")

    # 提取号码有效号码
    def get_validPhone(self):
        return self.get_element_text(sendMsg.msg_validPhone, "提取号码有效号码")

    # 点击发送成功-确认
    def send_suceedPop(self):
        self.click_element(sendMsg.send_affirm, "发送普通短信_确认")

    # 点击发送成功-取消
    def send_filedPop(self):
        self.click_element(sendMsg.send_close, "发送普通短信_取消")

    # 立即发送
    def send_immediately(self):
        self.click_element(sendMsg.send_now, "发送普通短信_选择立即发送方式")

    # 定时发送
    def send_timeingMode(self):
        self.click_element(sendMsg.timeing_send, "发送普通短信_选择定时发送方式")

    # 定时时间
    def send_normal_timeing(self, timeing):
        # 取消readonly属性变为可输入
        js = 'document.getElementById("timingTime").removeAttribute("readonly")'
        self.driver.execute_script(js)
        self.input_text(sendMsg.time_alarm, "发送普通短信_定时时间", timeing)

    # 重置
    def send_reset(self):
        self.click_element(sendMsg.send_reset, "发送普通短信_点击重置")

    # 退订设置
    def send_unsubscribe(self):
        self.click_element(sendMsg.msg_unsubscribe, "发送普通短信_点击退订设置")

    # 链接跟踪
    def send_link(self):
        self.click_element(sendMsg.msg_link, "发送普通短信_点击链接跟踪")

    # 关闭链接跟踪弹窗
    def send_closeLink(self):
        self.click_element(sendMsg.msg_Closelink, "发送普通短信_关闭链接跟踪")