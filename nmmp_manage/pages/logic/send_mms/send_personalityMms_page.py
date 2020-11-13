# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 发送个性彩信
import time

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_mms.send_personalityMms_locator import SendPersoalitynMmsLocator as sendpMms


class SendPerMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 导入收件号码
    def send_pMmsUpload(self, phone):
        self.input_text(sendpMms.phone_upload, "发送个性彩信_导入收件号码", phone)
        self.click_element(sendpMms.file_upload, "发送个性彩信_导入")

    # 输入标题内容
    def send_content(self, title, content, images):
        self.input_text(sendpMms.mms_title, "发送个性彩信_彩信标题", title)
        self.input_text(sendpMms.mms_content, "发送个性彩信_彩信文字", content)
        self.input_text(sendpMms.images_upload, "发送彩信_制作彩信本地上传", images)
        self.click_element(sendpMms.inset_variable, "发送个性彩信_插入变量")

    # 点击预处理
    def send_submit(self):
        self.click_element(sendpMms.mms_pretreatment, "发送个性彩信_预处理")

    # 点击立即发送
    def send_promptly(self):
        self.click_element(sendpMms.promptly_send, "发送个性彩信_立即发送")

    def func_basic(self, data1, data2, data3, data4):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '彩信')
        MenuUtils(self.driver).menu_tab('li', '发送个性彩信')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_1004')  # 获取iframe
        # SendPerMmsPage(self.driver).send_pMmsUpload(data1)
        self.input_text(sendpMms.phone_upload, "发送个性彩信_导入收件号码", data1)
        self.click_element(sendpMms.file_upload, "发送个性彩信_导入")
        time.sleep(2)
        # SendPerMmsPage(self.driver).send_content(data2, data3, data4)
        self.input_text(sendpMms.mms_title, "发送个性彩信_彩信标题", data2)
        self.input_text(sendpMms.mms_content, "发送个性彩信_彩信文字", data3)
        self.input_text(sendpMms.images_upload, "发送彩信_制作彩信本地上传", data4)
        self.click_element(sendpMms.inset_variable, "发送个性彩信_插入变量")
        MenuUtils(self.driver).menu_tab('li', '姓名')
        time.sleep(2)

    # 返回短信审核箱需要验证的列
    def func_checkResults(self, nature):
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_45', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(5)
        # 点击刷新按钮
        self.click_element(sendpMms.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature)
        return msg_checkTrOne

    # 结果验证（短信审核箱、已发短信）
    def func_results(self, nature1, textOne, redirect, iframe1, nature2,  textTwo):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_45', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(12)
        self.click_element(sendpMms.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        if msg_dispose.text == '处理成功':
            msg_checkTrOne = getProperty(self.driver).get_pro(msg_checkTr, nature1)
            # 判断审核状态是否与预期一致
            if msg_checkTrOne.text == textOne:
                self.driver.switch_to.default_content()  # 释放iframe
                time.sleep(2)
                MenuUtils(self.driver).menu_tab('li', redirect)
                time.sleep(2)
                comm_frame(self.driver).Frame(iframe1)
                # 连接数据库循环判断已发短信是否有对应id
                Arr = connectMysql(self.driver).connect_mysql('192.168.0.155', 'nemmp_common', "SELECT * FROM `mms_task_contact`",
                                                          int(getDataId), 0)
                if len(Arr) > 0:
                    for id in Arr:
                        # 通过dataid属性定位元素
                        msg_alreadyTr = self.driver.find_element_by_css_selector('[dataid="' + str(id) + '"]')
                        # 获取属性为'sendStatus'的元素
                        msg_text = getProperty(self.driver).get_pro(msg_alreadyTr, nature2)
                        msg_check = getProperty(self.driver).get_pro(msg_alreadyTr, 'statusCodeEn')
                        # 判断发送状态与预期是否相符
                        if msg_check.text == '余额不足':
                            print(msg_check.text)
                            break
                        elif textTwo != msg_text.text:
                            print(msg_alreadyTr.text)
                            print('状态代码' +msg_text.text)
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



