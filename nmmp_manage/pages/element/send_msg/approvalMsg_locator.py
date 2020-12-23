# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2
# @Author  : wangyufeng
# @Remark: 生日短信页面元素定位
from selenium.webdriver.common.by import By


class approvalMsgLocator:
    # 取消
    approvalMsg_cancel = (By.XPATH, '/html/body/div[1]/div[1]/div/a[1]')
    # 修改重发
    approvalMsg_alterRetry = (By.XPATH, '/html/body/div[1]/div[1]/div/a[2]')
    # 号码明细
    approvalMsg_phoneDetail = (By.XPATH, '/html/body/div[1]/div[1]/div/a[3]')
    # 导出数据
    approvalMsg_derive = (By.XPATH, '//*[@id="export"]/a')
    # 导出当前页选中的数据
    approvalMsg_selectDerive = (By.XPATH, '//*[@id="export"]/ul/li[1]/a')
    # 导出列表全部数据
    approvalMsg_allDerive = (By.XPATH, '//*[@id="export"]/ul/li[2]/a')
    # 页面顶部提示信息
    approvalMsg_message = (By.XPATH, '/html/body/div[6]')
    # 获取列表长度
    approvalMsg_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')
    # 导出全部数据弹窗提示语
    approvalMsg_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 导出全部数据弹窗关闭
    approvalMsg_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')