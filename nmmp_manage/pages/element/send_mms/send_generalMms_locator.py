# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 发送普通彩信
from selenium.webdriver.common.by import By



class SendMmsLocator:

    # 收件号码
    mms_phone = (By.XPATH, '//*[@id="receiver"]')
    # 提取号码
    mms_extractPhone = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[6]/a[1]')
    # 选择彩信产品
    mms_select = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[7]/div[2]/a')
    # 立即发送
    mms_promptly = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[10]/div[2]/div[1]/span[1]')
    # 定时发送
    mms_timeing = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[10]/div[2]/div[2]/span[1]')
    # 定时时间输入框
    time_alarm = (By.XPATH, '//*[@id="timingTime"]')
    # 提交发送
    mms_submit = (By.XPATH, '//*[@id="receiverForm"]/div[1]/div[3]/div[12]/a[1]')
    # 勾选产品
    mms_product = (By.XPATH, '//*[@id="table_content"]/tbody/tr[1]/td[1]/span')
    # 确认选择
    mms_affirm = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 关闭弹窗
    mms_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
    # 确认
    mms_send = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 取消
    mms_cancel = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')
    # 平台审核箱刷新刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/div/a[6]')


