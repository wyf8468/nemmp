# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17
# @Author  : wangyufeng
# @Remark: 发送普通视频短信页面模块封装
import time
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_videoMsg.send_generalVideoMsg_locator import SendVideoMsgLocator as videoMsgLoc
from nmmp_manage.common.comm_extractDigital import comm_extractDigital as ced


class SendVedioMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    def func_basic(self, data, value, time_timeing, valueOne):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '视频短信')
        MenuUtils(self.driver).menu_tab('li', '发送普通视频短信')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_1886')  # 获取iframe
        self.input_text(videoMsgLoc.videoMsg_phone, "发送普通视频短信_输入收件号码", data)
        self.click_element(videoMsgLoc.videoMsg_extract, "发送普通视频短信_提取号码")
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        self.click_element(videoMsgLoc.videoMsg_close, "发送普通视频短信_点击关闭弹窗")
        comm_frame(self.driver).Frame('mainFrame_1886')  # 获取iframe
        self.click_element(videoMsgLoc.videoMsg_product, "发送普通视频短信_点击选择视频短信产品")
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_goChoseVideoSmsProduct')  # 获取iframe
        self.click_element(videoMsgLoc.videoMsg_check, "发送普通视频短信_勾选复选框")
        self.click_element(videoMsgLoc.videoMsg_affirm, "发送普通视频短信_确认选择")
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_1886')  # 获取iframe
        if value == '立即发送':
            self.click_element(videoMsgLoc.videoMsg_now, "发送普通视频短信_立即发送")
        elif value == '定时发送':
            self.click_element(videoMsgLoc.videoMsg_timeing, "发送普通视频短信_定时发送")
            # 取消readonly属性变为可输入
            js = 'document.getElementById("timingTime").removeAttribute("readonly")'
            self.driver.execute_script(js)
            # 输入定时时间
            self.input_text(videoMsgLoc.time_alarm, "发送普通短信_定时时间", time_timeing)
        self.click_element(videoMsgLoc.videoMsg_submit, "发送普通视频短信_提交发送")
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        if valueOne == '确认发送':
            self.click_element(videoMsgLoc.videoMsg_confirm, "发送普通视频短信_点击确定")
        else:
            self.click_element(videoMsgLoc.videoMsg_cancel, "发送普通视频短信_点击取消")
        return time_timeing

# 结果验证（短信审核箱、已发短信）
    def func_results(self, nature1, textOne, redirect, iframe1, nature2, nature3, textTwo):
        temp = True
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_1878', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        # 获取短信审核箱中提交过来的审核状态
        time.sleep(24)
        self.click_element(videoMsgLoc.msg_refresh, "短信审核箱_刷新")
        msg_checkTr = self.driver.find_element_by_css_selector('[dataid="' + str(getDataId) + '"]')
        msg_dispose = getProperty(self.driver).get_pro(msg_checkTr, 'handleStatusStr')
        count = self.get_element_text(videoMsgLoc.videoMsg_count, "视频短信审核箱——列表条数")
        count = int(ced(self.driver).comm_extractDigital(count))
        print(count)
        if count != 0:
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
                    Arr = connectMysql(self.driver).connect_mysql('192.168.0.155', 'nemmp_common', "SELECT * FROM `video_sms_task_contact`",
                                                          int(getDataId), 0)
                    if len(Arr) > 0:
                        for id in Arr:
                            # 通过dataid属性定位元素
                            msg_alreadyTr = self.driver.find_element_by_css_selector('[dataid="' + str(id) + '"]')
                            # 获取属性为'remark'的元素
                            msg_text = getProperty(self.driver).get_pro(msg_alreadyTr, nature2)
                            # 获取属性为'statusCode'的元素
                            msg_remark = getProperty(self.driver).get_pro(msg_alreadyTr, nature3)
                            # 判断发送状态与预期是否相符
                            if textTwo != msg_text.text:
                                print(msg_alreadyTr.text)
                                print(msg_text.text)
                                print('状态代码：' + msg_remark)
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
            print('列表没有数据')
            temp = False
        return temp
