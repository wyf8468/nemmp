# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22
# @Author  : wangyufeng
# @Remark: 已发视频短信页面元素定位
from selenium.webdriver.common.by import By


class alreadyVideoMsgLocator:
    # 预览
    alreadyVideo_preview = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 导出
    alreadyVideo_derive = (By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    # 页面顶部提示信息
    alreadyVideo_message = (By.XPATH, '/html/body/div[6]')
    # 获取列表长度
    alreadyVideo_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')
    # 弹窗提示语
    alreadyVideo_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 弹窗提示语-关闭
    alreadyVideo_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')