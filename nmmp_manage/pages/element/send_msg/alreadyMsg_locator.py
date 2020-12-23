# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  : wangyufeng
# @Remark: 已发短信页面元素定位
from selenium.webdriver.common.by import By


class alreadyMsgLocator:
    # 编辑重发
    already_details = (By.XPATH, '/html/body/div[1]/div[2]/a[1]')
    # 时间段导出
    already_timeDerive = (By.XPATH, '//*[@id="DateExport"]')
    # 选择开始时间
    already_beginTime = (By.XPATH, '//*[@id="startTime"]')
    # 选择结束时间
    already_finishTime = (By.XPATH, '//*[@id="endTime"]')
    # 时间段导出-导出
    already_timeAffirm = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 时间段导出-取消
    already_timeCancel = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')
    # 导出
    already_derive = (By.XPATH, '/html/body/div[1]/div[2]/a[3]')
    # 页面顶部提示信息
    already_message = (By.XPATH, '/html/body/div[6]')
    # 弹窗提示信息//*[@id="msgBoxId"]/div[3]/div/a
    already_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/div/span[2]')
    # 弹窗提示信息-关闭
    already_alterClose = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a')
    # 列表条数
    already_count = (By.XPATH, '//*[@id="pageing"]/div[2]/span[1]')
