# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/04
# @Author  : wangyufeng
# @Remark: 发送普通短信页面模块封装
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_msg_locator import SendMsgLocator as sendMsg


class SendMsgPage(seleniumUtils):
    # 发送普通短信
    @classmethod
    def send_normal_msg(self, enterMode, text):
        self.input_text(sendMsg.enter_mode, "发送普通短信_输入手机号", enterMode)
        self.input_text(sendMsg.msg_content, "发送普通短信_输入短信内容", text)
        self.click_element(sendMsg.send_now, "发送普通短信_选择立即发送方式")
        self.click_element(sendMsg.timeing_send, "发送普通短信_选择定时发送方式")
        self.click_element(sendMsg.send_submit, "发送普通短信_点击提交发送")
    # 获取登录失败提示信息
    def get_errorMsg(self):
        return self.get_element_text(sendMsg.send_error, "提交失败提示！")
        # 第一步：填写“收件号码”区域
        # 第二部：选择“短信签名”  ？？自己创建签名-公共数据
        # 第三步：填写短信内容
        # 第四步：选择“项目名称”
        # 第五步:发送方式
        # 第六步：点击

# ______________________________________send_normal_msg________________________________

    def write_recive_nunm(self, ):
        def __init__(self):
            pass
        # 第一步：选择TAB页


        # 第二步： 输入信息

        # 第三步：


    # def select_msg_sign(self):

    # def write_msg_context(self):

    # def select_project_name(self):

    # def select_send_fun(self):

    # def click(self):


    #______________________________________common________________________________


