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
    # 请输入发送邮址
    gemail_mailAddress = (By.XPATH, '//*[@id="inputEmails"]')
    # 请输入发送邮址
    gemail_send = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')



