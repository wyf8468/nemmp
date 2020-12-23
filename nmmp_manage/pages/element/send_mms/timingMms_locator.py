# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17
# @Author  : wangyufeng
# @Remark: 定时彩信页面元素定位
from selenium.webdriver.common.by import By


class timingMmsLocator:
    # 取消
    timingMms_cancel = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 彩信预览
    timingMms_preview = (By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    # 页面顶部提示语
    timingMms_message = (By.XPATH, '/html/body/div[6]')
    # 弹窗提示语
    # timingMms_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 弹窗提示语-关闭
    # timingMms_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
    # 列表记录数
    timingMms_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')