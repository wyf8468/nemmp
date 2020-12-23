# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17
# @Author  : wangyufeng
# @Remark: 发送普通视频短信页面模块封装
import time
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.connectMysql import connectMysql
from nmmp_manage.common.fileUpload import UpLoad_File
from nmmp_manage.common.getLists import getList
from nmmp_manage.common.get_property import getProperty
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_videoMsg.makeVideoMsg_locator import makeVMsgLocator as smvl


class makeVedioMsgPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    def func_basic(self, name, count, content, filePath, value):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '视频短信')
        MenuUtils(self.driver).menu_tab('li', '制作视频短信')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_1885')  # 获取iframe
        self.input_text(smvl.videoMsg_name, "制作视频短信输入标题", name)
        if count == 0:
            MenuUtils(self.driver).menu_tab('li', '插入文本')
            self.input_text(smvl.videoMsg_content_1, "制作视频短信输入文本内容", content)
            MenuUtils(self.driver).menu_tab('li', '插入视频')
            self.click_element(smvl.videoMsg_video_1, "制作视频短信-上传视频文件")
            UpLoad_File(filePath)
        elif count == 1:
            MenuUtils(self.driver).menu_tab('li', '插入视频')
            self.click_element(smvl.videoMsg_video_2, "制作视频短信-上传视频文件")
            UpLoad_File(filePath)
            MenuUtils(self.driver).menu_tab('li', '插入文本')
            self.input_text(smvl.videoMsg_content_2, "制作视频短信输入文本内容", content)
        elif count == 2:
            MenuUtils(self.driver).menu_tab('li', '插入图片')
            self.click_element(smvl.videoMsg_images_1, "制作视频短信-上传图片文件")
            UpLoad_File(filePath)
            MenuUtils(self.driver).menu_tab('li', '插入文本')
            self.input_text(smvl.videoMsg_content_2, "制作视频短信输入文本内容", content)
        elif count == 3:
            MenuUtils(self.driver).menu_tab('li', '插入文本')
            self.click_element(smvl.videoMsg_content_1, "制作视频短信-输入文本内容")
            MenuUtils(self.driver).menu_tab('li', '插入图片')
            self.input_text(smvl.videoMsg_images_2, "制作视频短信上传图片", content)
            UpLoad_File(filePath)
        time.sleep(2)
        self.click_element(smvl.videoMsg_saveReviews, "制作视频短信-点击提交审核")
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        if value == "确认":
            self.click_element(smvl.videoMsg_affirm, "制作视频短信-点击确认")
        else:
            self.click_element(smvl.videoMsg_close, "制作视频短信-点击关闭")








