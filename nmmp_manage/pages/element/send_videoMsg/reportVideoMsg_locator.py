# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : wangyufeng
# @Remark: 报备中心页面元素定位
from selenium.webdriver.common.by import By


class reportVideoMsgLocator:
    # 取消
    reportVideo_cancel = (By.XPATH, '/html/body/div[1]/div[1]/a[4]')
    # 预览
    reportVideo_preview = (By.XPATH, '/html/body/div[1]/div[1]/a[6]')
    # 编辑
    reportVideo_compile = (By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    # 删除
    reportVideo_delete = (By.XPATH, '/html/body/div[1]/div[1]/a[3]')
    # 提交审核
    reportVideo_audit = (By.XPATH, '/html/body/div[1]/div[1]/a[5]')
    # 导出
    reportVideo_derive = (By.XPATH, '/html/body/div[1]/div[1]/a[7]')
    # 页面顶部提示信息
    reportVideo_message = (By.XPATH, '/html/body/div[6]')
    # 获取列表长度
    reportVideo_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')
    # 弹窗提示语
    reportVideo_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 弹窗提示语-关闭
    reportVideo_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')