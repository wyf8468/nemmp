# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 发送个性彩信
from selenium.webdriver.common.by import By



class SendPersoalitynMmsLocator:

    # 文件导入
    phone_upload = (By.XPATH, '//*[@id="upload"]')
    # 导入
    file_upload = (By.XPATH, '//*[@id="uploadPhoneNumber"]')
    # 彩信标题
    mms_title = (By.XPATH, '//*[@id="cxtitle"]')
    # 彩信文字
    mms_content = (By.XPATH, '//*[@id="cxcontent"]')
    # 上传图片
    images_upload = (By.XPATH, '//*[@id="uploadPicture"]')
    # 插入变量
    inset_variable = (By.XPATH, '//*[@id="placeholderId"]')
    # 预处理
    mms_pretreatment = (By.XPATH, '//*[@id="submitGxhMmsOk"]')
    # 立即发送
    promptly_send = (By.XPATH, '//*[@id="sendGxhMms"]')
    # 定时发送
    timeing_send = (By.XPATH, '//*[@id="sendGxhMms"]')
    # 平台审核箱刷新刷新
    msg_refresh = (By.XPATH, '/html/body/div[1]/div[1]/div/a[6]')