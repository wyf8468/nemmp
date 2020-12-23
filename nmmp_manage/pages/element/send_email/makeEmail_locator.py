# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : wangyufeng
# @Remark: 制作邮件模板元素定位
from selenium.webdriver.common.by import By


class makemailLocator:
    # 模板名称
    memail_tile = (By.XPATH, '//*[@id="mailTemplateName"]')
    # 选择普通
    memail_general = (By.XPATH, '//*[@id="defaultRadioBox"]')
    # 选择个性
    memail_personality = (By.XPATH, '//*[@id="optionalRadioBox"]')
    # 选择插入的变量
    memail_variable = (By.XPATH, '//*[@id="submitGroup"]')
    # 输入内容
    memail_content = (By.XPATH, '/html/body')
    # 保存
    memail_save = (By.XPATH, '//*[@id="save"]')

