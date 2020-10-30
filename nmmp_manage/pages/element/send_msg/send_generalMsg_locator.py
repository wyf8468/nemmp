# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/03
# @Author  : wangyufeng
# @Remark: 发送普通短信页面元素定位
from selenium.webdriver.common.by import By



class SendMsgLocator:

    # 收件号码-tab切换(父节点)
    # enter_mode = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/ul')
    # 收件号码-手动输入（textarea）
    receipt_phone = (By.XPATH, '//*[@id="receiver"]')
    # 收件号码-清除按钮（父节点）
    # clear_btn = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/div[4]')
    # 短信签名（signatureId）
    msg_signatures = (By.XPATH, '//input[@id="signatureId"]')
    # 短信内容-textarea（sendContent）
    msg_content = (By.XPATH, '//*[@id="sendContent"]')
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
    time_alarm = (By.XPATH, '//*[@id="timingTime"]')
    # 错误提示
    send_error = (By.XPATH, '/html/body/div[6]')
    # 提交发送
    send_submit = (By.XPATH, '//*[@id="pNode"]/div[1]/div[2]/div[3]/div[6]/a[1]')
    # 重置
    send_reset = (By.XPATH, '//*[@id="pNode"]/div[1]/div[2]/div[3]/div[6]/a[2]')
    # 确认发送
    send_affirm = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 取消
    send_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')
    # 弹窗内的提示信息
    send_hint = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div')
    # iframe内部提示
    send_insidHint = (By.XPATH, '//*[@id="pNode"]/div[1]/div[1]/div[2]/div[2]/div')
    # 关闭链接跟踪
    msg_Closelink= (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
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
    # 刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/div/a[4]')
    # 短信签名
    msg_signature = (By.XPATH, '//*[@id="signatureId"]')
    # 项目名称
    msg_item = (By.XPATH, '//*[@id="projectID"]')







