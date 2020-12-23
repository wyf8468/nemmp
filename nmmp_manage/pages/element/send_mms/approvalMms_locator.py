# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16
# @Author  : wangyufeng
# @Remark: 平台彩信审核箱页面元素定位
from selenium.webdriver.common.by import By


class approvalMmsLocator:
    # 取消
    approvalMms_cancel = (By.XPATH, '/html/body/div[1]/div[1]/div/a[1]')
    # 修改重发
    approvalMms_againSend = (By.XPATH, '/html/body/div[1]/div[1]/div/a[2]')
    # 号码明细
    approvalMms_detail = (By.XPATH, '/html/body/div[1]/div[1]/div/a[3]')
    # 彩信预览
    approvalMms_preview = (By.XPATH, '/html/body/div[1]/div[1]/div/a[4]')
    # 导出
    approvalMms_derive = (By.XPATH, '/html/body/div[1]/div[1]/div/a[5]')
    # 页面顶部提示语
    approvalMms_message = (By.XPATH, '/html/body/div[6]')
    # 弹窗提示语
    approvalMms_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 弹窗提示语-关闭
    approvalMms_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
    # 列表记录数
    approvalMms_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')