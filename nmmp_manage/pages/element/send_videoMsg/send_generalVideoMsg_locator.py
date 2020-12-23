# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17
# @Author  : wangyufeng
# @Remark: 发送普通视频短信元素定位
from selenium.webdriver.common.by import By


class SendVideoMsgLocator:

    # 输入收件人
    videoMsg_phone = (By.XPATH, '//*[@id="receiver"]')
    # 提取号码
    videoMsg_extract = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[6]/a[1]')
    # 提取号码成功后关闭弹窗
    videoMsg_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
    # 选择视频短信产品
    videoMsg_product = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[7]/div[2]/a')
    # 选择视频短信产品第一个产品
    videoMsg_check = (By.XPATH, '//*[@id="table_content"]/tbody/tr[1]/td[1]/span')
    # 确认选择
    videoMsg_affirm = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 提交发送
    videoMsg_submit = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[11]/a[1]')
    # 确认
    videoMsg_confirm = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 立即发送
    videoMsg_now = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[9]/div[2]/div[1]/span[1]')
    # 定时发送
    videoMsg_timeing = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[9]/div[2]/div[2]/span[1]')
    # 定时时间
    time_alarm = (By.XPATH, '//*[@id="timingTime"]')
    # 取消发送
    videoMsg_cancel = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')
    # 刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/a[4]')
    # 列表条数
    videoMsg_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')

