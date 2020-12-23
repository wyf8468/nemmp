# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : wangyufeng
# @Remark: 邮件审核箱页面元素定位
from selenium.webdriver.common.by import By


class approvalEmailLocator:
    # 取消
    approvalEmail_cancel = (By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    # 修改重发
    approvalEmail_alterRetry = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 邮址明细
    approvalEmail_Detail = (By.XPATH, '/html/body/div[1]/div[1]/a[3]')
    # 下载
    approvalEmail_upDown = (By.XPATH, '/html/body/div[1]/div[1]/a[4]')
    # 预览
    approvalEmail_preview = (By.XPATH, '/html/body/div[1]/div[1]/a[5]')
    # 导出
    approvalEmail_derive = (By.XPATH, '/html/body/div[1]/div[1]/a[6]')
    # 页面顶部提示信息
    approvalEmail_message = (By.XPATH, '/html/body/div[6]')
    # 获取列表长度
    approvalEmail_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')
    # 导出全部数据弹窗提示语
    approvalEmail_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 导出全部数据弹窗关闭
    approvalEmail_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')