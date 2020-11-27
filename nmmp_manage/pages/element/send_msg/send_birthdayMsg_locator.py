# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送生日短信页面元素定位
from selenium.webdriver.common.by import By


class SendBirthMsgLocator:
    # 收件号码-文件导入（导入）
    birthday_receipt = (By.XPATH, '//*[@id="uploadPhoneNumber"]')
    # 短信内容
    birthday_content = (By.XPATH, '//*[@id="sendContent"]')
    # 发送时间-天
    birthday_days = (By.XPATH, '//*[@id="dayId"]')
    # 发送时间-时
    birthday_hour = (By.XPATH, '//*[@id="hourId"]')
    # 发送时间-分
    birthday_minute = (By.XPATH, '//*[@id="minId"]')
    # 退订设置
    birthday_tuid = (By.XPATH, '//*[@id="tuidingSelectID"]')
    # 预处理
    birthday_dispose = (By.XPATH, '//*[@id="sumbit"]')
    # 确认
    birthday_affirm = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/div/a[4]')


