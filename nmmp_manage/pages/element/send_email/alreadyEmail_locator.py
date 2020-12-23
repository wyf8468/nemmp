# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : wangyufeng
# @Remark: 已发邮件页面元素定位
from selenium.webdriver.common.by import By


class alreadyEmailLocator:
    # 预览
    alreadyEmail_preview = (By.XPATH, '//*[@id="preview"]')
    # 重新发送
    alreadyEmail_alterSend = (By.XPATH, '//*[@id="reSend"]')
    # 软退一键重发
    alreadyEmail_keyResend = (By.XPATH, '//*[@id="softBounce"]')
    # 软退一键重发-取消
    alreadyEmail_keyResend_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')
    # 软退一键重发-保存
    alreadyEmail_keyResend_save = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 导出
    alreadyEmail_derive = (By.XPATH, '//*[@id="export"]')
    # 页面顶部提示信息
    alreadyEmail_message = (By.XPATH, '/html/body/div[6]')
    # 获取列表长度
    alreadyEmail_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')
    # 导出全部数据弹窗提示语
    alreadyEmail_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 导出全部数据弹窗关闭
    alreadyEmail_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')