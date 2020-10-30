# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送普通邮件元素定位
from selenium.webdriver.common.by import By



class SendGemailMsgLocator:

    # 输入收件人
    gemail_receive = (By.XPATH, '//*[@id="receiver"]')
    # 提取邮址
    gemail_extract = (By.XPATH, '//*[@id="receiverForm"]/div[3]/div[4]/a[1]')
    # 提取邮址关闭弹窗
    gemail_extractClose = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
    # 选择模板
    gemail_select = (By.XPATH, '//*[@id="allTemplateView"]')
    # 勾选复选框
    gemail_checkbox = (By.XPATH, '//*[@id="table_content"]/tbody/tr[1]/td[1]/span')
    # 确认选择模板
    gemail_checkboxAffirm = (By.XPATH, '/html/body/div[1]/a[1]')
    # 输入发件人名称
    gemail_senderName = (By.XPATH, '//*[@id="sendMailName"]')
    # 输入邮件主题
    gemail_theme = (By.XPATH, '//*[@id="title"]')
    # 测试发送
    gemail_submit = (By.XPATH, '//*[@id="testSending"]')
    # 提交发送
    gemail_commit = (By.XPATH, '//*[@id="send"]')
    # 请输入发送邮址
    gemail_mailAddress = (By.XPATH, '//*[@id="inputEmails"]')
    # 确认发送
    gemail_send = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 取消发送
    gemail_cancel = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')
    # 发件人域名
    gemail_domain = (By.XPATH, '//*[@id="sendMailAddress"]')
    # 立即发送
    gemail_now = (By.XPATH, '//*[@id="receiverForm"]/div[3]/div[10]/div[2]/span[1]')
    # 定时发送
    gemail_timeing = (By.XPATH, '//*[@id="receiverForm"]/div[3]/div[10]/div[2]/span[3]')
    # 输入定时时间
    time_timeing = (By.XPATH, '//*[@id="timingTime"]')
    # 审核刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/a[7]')
    # 提示信息
    msg_hint = (By.XPATH, '/html/body/div[6]')
    # 确定
    msg_confirm = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 已发刷新
    video_refresh = (By.XPATH, '//*[@id="refurbish"]')





