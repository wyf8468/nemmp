# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/03
# @Author  : wangyufeng
# @Remark: 发送普通短信页面元素定位

from selenium.webdriver.common.by import By


class SendMsgLocator:

    def __init__(self):
        pass

    # 收件号码-tab切换(父节点)
    enter_mode = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/ul')
    # 收件号码-手动输入（textarea）
    receipt_num = (By.XPATH, '//*[@id="receiver"]')
    # 收件号码-清除按钮（父节点）
    clear_btn = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/div[4]')
    # 短信签名（signatureId）
    msg_signatures = (By.XPATH, '//input[@id="signatureId"]')
    # 短信内容-textarea（sendContent）
    msg_content = (By.XPATH, '')
    # 短信内容-退订设置（tuidingSelectID）
    msg_unsubscribe = (By.XPATH, '//*[@id="tuidingSelectID"]')
    # 短信内容-链接跟踪（linkSettingSelectID）
    msg_link = (By.XPATH, '//*[@id="linkSettingSelectID"]')
    # 项目名称
    project_name = (By.XPATH, '//*[@id="projectID"]')
    # 发送方式-立即发送
    send_now = (By.XPATH, '//*[@id="pNode"]/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/span[1]')
    # 发送方式-定时发送
    timeing_send = (By.XPATH, '//*[@id="pNode"]/div[1]/div[2]/div[3]/div[4]/div[2]/div[2]/span[1]')
    # 定时时间
    time_alarm = (By.XPATH, '//input[@id="timingTime"]')
    # 错误提示
    send_error = (By.XPATH, '/html/body/div[6]')
    # 提交发送
    send_submit = (By.XPATH, '//*[@id="pNode"]/div[1]/div[2]/div[3]/div[6]/a[1]')
    # 重置
    send_reset = (By.XPATH, '//*[@id="pNode"]/div[1]/div[2]/div[3]/div[6]/a[2]')






