# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  : wangyufeng
# @Remark: 定时短信页面元素定位
from selenium.webdriver.common.by import By


class timingMsgLocator:
    # 取消
    timing_cancel = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 页面顶部提示信息
    timing_message = (By.XPATH, '/html/body/div[6]')
