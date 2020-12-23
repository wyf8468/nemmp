# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11
# @Author  : wangyufeng
# @Remark: 发送个性短信页面模块封装
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.get_property import getProperty
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_personalityMsg_locator import SendPersonMsgLocator as sendPerMsg
from nmmp_manage.common.menuUtils import *
from nmmp_manage.common.fileUpload import *
from nmmp_manage.common.getLists import *
from nmmp_manage.common.editfiles import editFiles


class SendPerMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送基础步骤
    def func_basics(self, data1, data2, value, time_timeing, vauleOne):
        # 进入发送个性短信页面
        MenuUtils(self.driver).menu_tab('li', '发送个性短信')
        self.driver.implicitly_wait(5)
        comm_frame(self.driver).Frame('mainFrame_27')  # 获取iframe
        # 点击导入按钮
        self.click_element(sendPerMsg.receipt_phone, "发送个性短信_点击导入")
        UpLoad_File(data1)
        self.input_text(sendPerMsg.msg_content, "发送个性短信_输入短信内容", data2)
        if value == '立即发送':
            self.click_element(sendPerMsg.send_now, "发送普通短信_选择立即发送方式")
        elif value == '定时发送':
            self.click_element(sendPerMsg.timeing_send, "发送普通短信_选择定时发送方式")
            # 取消readonly属性变为可输入
            js = 'document.getElementById("timingTime").removeAttribute("readonly")'
            self.driver.execute_script(js)
            # 输入定时时间
            self.input_text(sendPerMsg.time_alarm, "发送普通短信_定时时间", time_timeing)
        # 预处理
        self.click_element(sendPerMsg.pre_processing, "发送个性短信_预处理")
        self.driver.switch_to.default_content()  # 释放iframe
        self.driver.implicitly_wait(5)
        if vauleOne == '确认发送':
            # 点击弹窗上的确认按钮
            self.click_element(sendPerMsg.send_ensure, "发送个性短信_确认")
        elif vauleOne == '取消发送':
            # 点击弹窗上的取消按钮
            self.click_element(sendPerMsg.send_close, "发送个性短信_取消")
        return time_timeing

    # 返回短信审核箱需要验证的列
    def func_checkResults(self, nature):
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_28', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(5)
        # 点击刷新按钮
        self.click_element(sendPerMsg.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature)
        return msg_checkTrOne

    # 结果验证（短信审核箱、已发短信）
    def func_results(self, nature1, textOne, redirect, iframe1, nature2, nature3, nature4, textTwo):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_28', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(12)
        self.click_element(sendPerMsg.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature1)
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        if msg_dispose.text == '处理成功':
            # 判断审核状态是否与预期一致
            if msg_checkTrOne.text == textOne:
                self.driver.switch_to.default_content()  # 释放iframe
                self.driver.implicitly_wait(5)
                MenuUtils(self.driver).menu_tab('li', redirect)
                self.driver.implicitly_wait(5)
                comm_frame(self.driver).Frame(iframe1)
                # 连接数据库循环判断已发短信是否有对应id
                Arr = connectMysql(self.driver).connect_mysql('192.168.0.152', 'nemmp_sms_zk', "SELECT * FROM `sms_task_contact_202012` ORDER BY create_date DESC",
                                                          int(getDataId), 0)
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
                            print('状态代码' + msg_status)
                            temp = False
                            break
                else:
                    print('找不到元素')
                    temp = False
            else:
                print(msg_checkTrOne.text)
                temp = False
        else:
            print(msg_checkTrOne.text)
            temp = False
        return temp



