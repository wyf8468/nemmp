# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11
# @Author  : wangyufeng
# @Remark: 彩信产品页面元素定位
from selenium.webdriver.common.by import By


class productsMmsLocator:
    # 制作彩信
    productsMms_make = (By.XPATH, '/html/body/div[1]/div[1]/a[1]')
    # 修改
    productsMms_modification = (By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    # 预览
    productsMms_preview = (By.XPATH, '/html/body/div[1]/div[1]/a[3]')
    # 删除
    productsMms_delete = (By.XPATH, '/html/body/div[1]/div[1]/a[4]')
    # 页面顶部提示信息
    productsMms_message = (By.XPATH, '/html/body/div[6]')
    # 弹窗提示语
    productsMms_alter = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div/p/span[2]')
    # 弹窗提示语-确定
    productsMms_sure = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 弹窗提示语-取消
    productsMms_cancel = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')