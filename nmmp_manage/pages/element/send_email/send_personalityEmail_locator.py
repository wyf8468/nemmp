# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 发送个性邮件元素定位
from selenium.webdriver.common.by import By



class SendPemailMsgLocator:

    # 浏览收件人
    pemail_receive = (By.XPATH, '//*[@id="upload"]')
    # 导入
    pemail_upload = (By.XPATH, '//*[@id="uploadMailTemplate"]')
    # 选择模板
    pemail_select = (By.XPATH, '//*[@id="allTemplateView"]')
    # 勾选复选框
    pemail_checkbox = (By.XPATH, '//*[@id="table_content"]/tbody/tr/td[1]/span')
    # 确认选择模板
    pemail_checkboxAffirm = (By.XPATH, '/html/body/div[1]/a[1]')
    # 输入发件人名称
    pemail_senderName = (By.XPATH, '//*[@id="sendMailName"]')
    # 输入发件人域名
    pemail_domain = (By.XPATH, '//*[@id="sendMailAddress"]')
    # 输入邮件主题
    pemail_theme = (By.XPATH, '//*[@id="title"]')
    # 提交发送
    pemail_submit = (By.XPATH, '//*[@id="send"]')
    # 确认
    pemail_affirm = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 插入变量
    pemail_variable = (By.XPATH, '//*[@id="submitVar"]')
    # 邮件审核箱刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/a[7]')

