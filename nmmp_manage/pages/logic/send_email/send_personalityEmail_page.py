# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 发送个性邮件模块封装
import time

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_email.send_personalityEmail_locator import SendPemailMsgLocator as speml


class SendPemailPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送个性邮件导入收件人
    def send_receive(self, receive):
        self.input_text(speml.pemail_receive, "发送个性邮件_选择模板", receive)
        self.click_element(speml.pemail_upload, "发送个性邮件_导入")
        self.click_element(speml.pemail_select, "发送个性邮件_选择模板")

    # 点击勾选复选框
    def send_checkbox(self):
        self.click_element(speml.pemail_checkbox, "发送个性邮件_勾选复选框")
        self.click_element(speml.pemail_checkboxAffirm, "发送个性邮件_勾选复选框确认选择模板")

    # 发送普通邮件，点击测试发送
    def send_senderName(self, senderName, theme):
        self.input_text(speml.pemail_senderName, "发送个性邮件_输入收件人名称", senderName)
        self.input_text(speml.pemail_domain, "发送个性邮件_输入邮件主题", 'marketing@send.szaisiou.com')
        self.input_text(speml.pemail_theme, "发送个性邮件_输入邮件主题", theme)
        self.click_element(speml.pemail_submit, "发送个性邮件_提交发送")

    # 输入发送邮址，确认发送
    def send_affirm(self):
        self.click_element(speml.pemail_affirm, "发送个性邮件_确认")

    def func_basic(self, data1, data2, data3):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '电子邮件')
        MenuUtils(self.driver).menu_tab('li', '发送管理')
        MenuUtils(self.driver).menu_tab('li', '发送个性邮件')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_310')  # 获取iframe
        # self.send_receive(data1)
        self.input_text(speml.pemail_receive, "发送个性邮件_选择模板", data1)
        self.click_element(speml.pemail_upload, "发送个性邮件_导入")
        self.click_element(speml.pemail_select, "发送个性邮件_选择模板")
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_goTemplateList')  # 获取iframe
        # self.send_checkbox()
        self.click_element(speml.pemail_checkbox, "发送个性邮件_勾选复选框")
        self.click_element(speml.pemail_checkboxAffirm, "发送个性邮件_勾选复选框确认选择模板")

        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_310')  # 获取iframe
        time.sleep(2)
        # self.send_senderName(data2, data3)
        self.input_text(speml.pemail_senderName, "发送个性邮件_输入收件人名称", data2)
        self.input_text(speml.pemail_domain, "发送个性邮件_输入邮件主题", 'marketing@send.szaisiou.com')
        self.input_text(speml.pemail_theme, "发送个性邮件_输入邮件主题", data3)
        self.click_element(speml.pemail_variable, "发送个性邮件_提交发送")
        MenuUtils(self.driver).menu_tab('li', '姓名')
        self.click_element(speml.pemail_submit, "发送个性邮件_提交发送")
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe

    # 结果验证
    def func_results(self, nature1, textOne, redirect, iframe1, nature2, nature3, textTwo, sgeml=None):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_106', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(60)
        # wait = WebDriverWait(driver, 20)
        self.click_element(speml.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        if msg_dispose.text == "处理完成":
            msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature1)
            # 判断审核状态是否与预期一致
            if msg_checkTrOne.text == textOne:
                self.driver.switch_to.default_content()  # 释放iframe
                time.sleep(2)
                MenuUtils(self.driver).menu_tab('li', redirect)
                time.sleep(2)
                comm_frame(self.driver).Frame(iframe1)
                time.sleep(20)
                # 连接数据库循环判断已发短信是否有对应id
                Arr = connectMysql(self.driver).connect_mysql('192.168.0.155', 'nemmp_common', "SELECT * FROM `mail_task_contact`",
                                                          int(getDataId), 0)
                if len(Arr) > 0:
                    for id in Arr:
                        # 通过dataid属性定位元素
                        msg_alreadyTr = self.driver.find_element_by_css_selector('[dataid="' + str(id) + '"]')
                        # 获取属性为'returnMsg'的元素
                        msg_text = getProperty(self.driver).get_pro(msg_alreadyTr, nature2)
                        msg_return = getProperty(self.driver).get_pro(msg_alreadyTr, nature3)
                        # 判断发送状态与预期是否相符
                        if textTwo != msg_text.text:
                            print(msg_alreadyTr.text)
                            print('状态：' +msg_text.text)
                            print('投递详情：' + msg_return.text)
                            temp = False
                            break
                else:
                    print('找不到元素')
                    temp = False
            else:
                print(msg_checkTrOne.text + '不等于入库成功（等待时间60s）')
                temp = False
        else:
            print(msg_dispose.text + '不等于处理完成')
            temp = False
        return temp