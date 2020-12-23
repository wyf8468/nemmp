# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  : wangyufeng
# @Remark: 生日短信页面元素定位
from selenium.webdriver.common.by import By


class birthdayMsgLocator:
    # 查看详情
    birthday_details = (By.XPATH, '//*[@id="toDetails"]')
    # 取消发送
    birthday_cancel = (By.XPATH, '//*[@id="toCancel"]')
    # 页面顶部提示信息
    birthday_message = (By.XPATH, '/html/body/div[6]')
