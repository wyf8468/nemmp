# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : wangyufeng
# @Remark: 已发彩信页面元素定位
from selenium.webdriver.common.by import By


class alreadyMmsLocator:
    # 彩信预览
    alreadyMms_preview = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 导出
    alreadyMms_derive = (By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    # 页面顶部提示语
    alreadyMms_message = (By.XPATH, '/html/body/div[6]')
    # 弹窗提示语
    alreadyMms_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 弹窗提示语-关闭
    alreadyMms_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
    # 列表记录数
    alreadyMms_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')