# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/04
# @Author  : wangyufeng
# @Remark: 发送普通短信页面模块封装
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_generalMsg_locator import SendMsgLocator as sendMsg
from nmmp_manage.common.comm_frame import *
import time
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


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
    def send_timeingMode(self, timeing):
        self.click_element(sendMsg.timeing_send, "发送普通短信_选择定时发送方式")
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

    # 短信审核箱_刷新
    def send_refresh(self):
        self.click_element(sendMsg.msg_refresh, "短信审核箱_刷新")

    # 选择短信签名
    def send_signature(self):
        self.click_element(sendMsg.msg_signature, "发送普通短信_短信签名")

    # 输入短信签名
    def send_input_signature(self, signature):
        self.input_text(sendMsg.msg_signature, "发送普通短信_短信签名", signature)

    # 选择项目名称
    def send_msg_item(self):
        self.click_element(sendMsg.msg_item, "发送普通短信_项目名称")

    # 验证提取收件号码数是否正确
    def func_verifyPhone(self, data1, data2, data3, data4):
        valid = ced(self.driver).comm_extractDigital(self.get_validPhone())
        temp = True
        if data1 == self.get_phoneNum():
            pass
        else:
            temp = False
            print('提取号码总数不正确')
            print(data1, self.get_phoneNum())
        if data2 == self.get_errorPhone():
            pass
        else:
            temp = False
            print(data2, self.get_errorPhone())
            print('提取错误号码数不正确')
        if data3 == self.get_repetitionPhone():
            pass
        else:
            temp = False
            print(data3, self.get_repetitionPhone())
            print('提取重复号码数不正确')
        if data4 == valid:
            pass
        else:
            temp = False
            print(data4, valid)
            print('提取有效号码数不正确')
        return temp

    # 发送流程步骤
    def func_basics(self, data1, data2, time_timeing, value):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        self.send_normal_msg(data1, data2)
        if value == '立即发送':
            self.send_immediately()
        else:
            self.send_timeingMode(time_timeing)
        self.send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe
        return time_timeing

    # 双回T提示语验证
    def func_doubleBasics(self, data1, data2, data3):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        self.send_normal_msg(data1, data2)
        self.send_immediately()  # 立即发送
        self.send_unsubscribe()  # 点击退订设置
        MenuUtils(self.driver).menu_tab('li', data3)
        self.send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe

    # 开启链接跟踪提示语验证
    def func_linkBasics(self, data1, data2, data3, data4):
        temp = True
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        self.send_normal_msg(data1, data2)
        self.send_immediately()  # 立即发送
        self.send_link()
        # 选择开启链接跟踪
        MenuUtils(self.driver).menu_tab('li', '开启')
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        if data3 == self.get_popMsg():
            self.send_closeLink()  # 关闭链接跟踪弹窗
            comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
            self.send_submit()  # 提交发送
            time.sleep(2)
            self.driver.switch_to.default_content()  # 释放iframe
            if data4 == self.get_popMsg():
                self.send_suceedPop()  # 点击弹窗上的确认发送按钮
            else:
                print(self.get_popMsg())
                temp = False
        else:
            print(self.get_popMsg())
            temp = False
        return temp

    # 返回短信审核箱需要验证的列
    def func_checkResults(self, nature):
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_28', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(2)
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature)
        return msg_checkTrOne

    # 结果验证（短信审核箱、已发短信）
    def func_results(self, nature1, textOne, redirect, iframe1, nature2, nature3, nature4, textTwo):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_28', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(8)
        self.send_refresh()
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature1)
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        if msg_dispose.text == '处理成功':
            # 判断审核状态是否与预期一致
            if msg_checkTrOne.text == textOne:
                self.driver.switch_to.default_content()  # 释放iframe
                time.sleep(2)
                MenuUtils(self.driver).menu_tab('li', redirect)
                time.sleep(2)
                comm_frame(self.driver).Frame(iframe1)
                # 连接数据库循环判断已发短信是否有对应id
                Arr = connectMysql(self.driver).connect_mysql('192.168.0.152', 'nemmp_sms_zk', "SELECT * FROM `sms_task_contact_202012` ORDER BY create_date DESC", int(getDataId), 0)
                if len(Arr) > 0:
                    for id in Arr:
                        # 通过dataid属性定位元素
                        msg_alreadyTr = self.driver.find_element_by_css_selector('[dataid="' + str(id) + '"]')
                        # 获取属性为'sendStatus'的元素
                        msg_text = getProperty(self.driver).get_pro(msg_alreadyTr, nature2)
                        # 获取属性为'statusCodeCh'的元素
                        msg_remark = getProperty(self.driver).get_pro(msg_alreadyTr, nature3)
                        # 获取状态码信息
                        msg_status = getProperty(self.driver).get_pro(msg_alreadyTr, nature4)
                        # 判断发送状态与预期是否相符
                        if textTwo != msg_text.text:
                            print(msg_alreadyTr.text)
                            print(msg_text.text)
                            print('代码注释：' + msg_remark.text)
                            print('状态代码'+msg_status)
                            temp = False
                            break
                else:
                    print('找不到元素')
                    temp = False
            else:
                print(msg_checkTrOne.text)
                temp = False
        else:
            print(msg_dispose.text)
            temp = False
        return temp









