# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13
# @Author  : wangyufeng
# @Remark: 发送普通视频短信元素定位
from selenium.webdriver.common.by import By


class makeVMsgLocator:
    # 输入标题
    videoMsg_name = (By.XPATH, '//*[@id="videoName"]')
    # 输入文本内容
    videoMsg_content_1 = (By.XPATH, '//*[@id="videoSms"]/div/div')
    # 上传视频
    videoMsg_video_1 = (By.XPATH, '//*[@id="videoSms"]/div[1]/a')
    # 上传图片
    videoMsg_images_1 = (By.XPATH, '//*[@id="videoSms"]/div/a')
    videoMsg_images_2 = (By.XPATH, '//*[@id="videoSms"]/div[1]/a')
    # 输入文本内容
    videoMsg_content_2 = (By.XPATH, '//*[@id="videoSms"]/div[1]/div')
    # 上传视频
    videoMsg_video_2 = (By.XPATH, '//*[@id="videoSms"]/div/a')
    # 提交审核
    videoMsg_saveReviews = (By.XPATH, '//*[@id="saveReview"]')
    # 保存
    videoMsg_save = (By.XPATH, '//*[@id="save"]')
    # 重置
    videoMsg_reset = (By.XPATH, '//*[@id="reset"]')
    # 确认
    videoMsg_affirm = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[1]')
    # 关闭
    videoMsg_close = (By.XPATH, '//*[@id="msgBoxId"]/div[3]/div/a[2]')