# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11
# @Author  : wangyufeng
# @Remark: 发送个性短信页面元素定位
from selenium.webdriver.common.by import By


class SendPersonMsgLocator:
    # 收件号码-文件导入（导入）
    receipt_phone = (By.XPATH, '//*[@id="uploadPhoneNumber"]')
    # 短信内容
    msg_content = (By.XPATH, '//*[@id="sendContent"]')
    # 预处理
    pre_processing = (By.XPATH, '//*[@id="pNode"]/div[1]/div[8]/a')
    # 弹窗-发送按钮
    send_ensure = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div[2]/div/a[1]')
    # 短信内容-退订设置（tuidingSelectID）
    msg_unsubscribe = (By.XPATH, '//*[@id="tuidingSelectID"]')
    # 短信内容-链接跟踪（linkSettingSelectID）
    msg_link = (By.XPATH, '//*[@id="linkSettingSelectID"]')
    # 发送方式-立即发送
    send_now = (By.XPATH, '//*[@id="pNode"]/div[1]/div[6]/div[2]/div[1]/span[1]')
    # 发送方式-定时发送
    timeing_send = (By.XPATH, '//*[@id="dingshiRadioBox"]')
    # 定时时间
    time_alarm = (By.XPATH, '//*[@id="timingTime"]')
    # 错误提示
    send_error = (By.XPATH, '/html/body/div[6]')
    # 取消
    send_close = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div[2]/div/a[2]')
    # 弹窗内的提示信息
    send_hint = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 短信计费
    msg_billing = (By.XPATH, '//*[@id="fs_number"]')
    # 号码总数
    msg_phoneSum = (By.XPATH, '//*[@id="phoneNumber"]')
    # 错误号码
    msg_errorPhone = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/div[4]/span/span[2]')
    # 重复号码
    msg_repetitionPhone = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/div[4]/span/span[3]')
    # 有效号码
    msg_validPhone = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/div[4]/span/span[4]')
    # 短信审核箱刷新刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/div/a[4]')
    # 短信签名
    msg_signature = (By.XPATH, '//*[@id="signatureId"]')
    # 项目名称
    msg_item = (By.XPATH, '//*[@id="projectID"]')
    # 插入变量
    msg_variate = (By.XPATH, '//*[@id="projectID"]')