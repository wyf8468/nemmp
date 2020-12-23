# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 制作彩信
from selenium.webdriver.common.by import By



class makeMmsLocator:

    # 彩信标题
    mms_title = (By.XPATH, '//*[@id="cxtitle"]')
    # 彩信文字
    mms_content = (By.XPATH, '//*[@id="cxcontent"]')
    # 本地上传
    mms_upload = (By.XPATH, '//*[@id="upload"]')
    # 立即保存
    mms_save = (By.XPATH, '/html/body/div[4]/a[1]')
