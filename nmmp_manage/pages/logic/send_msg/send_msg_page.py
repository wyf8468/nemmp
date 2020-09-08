# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/04
# @Author  : wangyufeng
# @Remark: 发送普通短信页面模块封装
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_msg_locator import SendMsgLocator as sendMsg


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
    # 获取登录失败提示信息
    def get_errorMsg(self):
        return self.get_element_text(sendMsg.send_error, "提交失败提示！")

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

    # 循环退订设置内容
    def send_retreat(self):
        retreatStr = ["关闭", "回T退", "回T退订", "TD退订", "回N退订", "退订回T", "退订回D"]
        for i in range(len(retreatStr) - 1):
            print(retreatStr[i])

    # 链接跟踪
    def send_link(self):
        self.click_element(sendMsg.msg_link, "发送普通短信_点击链接跟踪")