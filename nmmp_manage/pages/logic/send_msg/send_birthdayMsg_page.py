# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送生日短信页面模块封装
import time

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.fileUpload import UpLoad_File
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_msg.send_birthdayMsg_locator import SendBirthMsgLocator as sbml
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas


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
        # 选择菜单到生日短信
        MenuUtils(self.driver).menu_tab('li', '直客短信')
        MenuUtils(self.driver).menu_tab('li', '发送生日短信')
        self.driver.implicitly_wait(5)
        comm_frame(self.driver).Frame('mainFrame_353')  # 获取iframe
        self.send_upload()
        UpLoad_File(data1)
        self.driver.implicitly_wait(5)
        self.click_element(sbml.birthday_tuid, "退订设置")
        MenuUtils(self.driver).menu_tab('li', '关闭')
        self.driver.implicitly_wait(5)
        self.send_birthday_msg(data2)
        MenuUtils(self.driver).menu_tab('li', data3)
        self.send_hour()
        MenuUtils(self.driver).menu_tab('li', data4)
        self.send_minute()
        MenuUtils(self.driver).menu_tab('li', data5)
        self.send_dispose()
        self.driver.switch_to.default_content()  # 释放iframe

    # 返回短信审核箱需要验证的列
    def func_checkResults(self, nature):
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_28', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(5)
        # 点击刷新按钮
        self.click_element(sbml.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_content = getProperty(self.driver).get_pro(msg_checkTr, 'sendContentStr')
        print(msg_content.text)
        print(msgDatas.birthday_success['content'])
        if msg_content.text == msgDatas.birthday_success['content']:
            msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature)
        else:
            print('短信审核箱里没有提交过来的生日短信任务')

        return msg_checkTrOne

    # 结果验证（短信审核箱、已发短信）
    def func_results(self, nature1, textOne, redirect, iframe1, nature2, nature3, nature4, textTwo, ):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_28', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(12)
        self.click_element(sbml.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature1)
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        msg_content = getProperty(self.driver).get_pro(msg_checkTr, 'sendContentStr')
        print(msg_content)
        print(msgDatas.birthday_success['content'])
        if msg_content.text == msgDatas.birthday_success['content']:
            if msg_dispose.text == '处理成功':
                # 判断审核状态是否与预期一致
                if msg_checkTrOne.text == textOne:
                    self.driver.switch_to.default_content()  # 释放iframe
                    self.driver.implicitly_wait(5)
                    MenuUtils(self.driver).menu_tab('li', redirect)
                    self.driver.implicitly_wait(5)
                    comm_frame(self.driver).Frame(iframe1)
                    # 连接数据库循环判断已发短信是否有对应id
                    Arr = connectMysql(self.driver).connect_mysql('192.168.0.152', 'nemmp_sms_zk', "SELECT * FROM `sms_task_birthday_contact`", int(getDataId), 0)
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
        else:
            print('短信审核箱里没有提交过来的生日短信任务')
            temp = False

        return temp



