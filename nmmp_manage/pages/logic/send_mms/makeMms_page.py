# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 制作彩信模板
import time

from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_mms.makeMms_locator import makeMmsLocator as sendMakeMms


class makeMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 发送彩信
    def send_makeMms(self, title, content, imgs):
        self.input_text(sendMakeMms.mms_title, "发送彩信_制作彩信标题", title)
        self.input_text(sendMakeMms.mms_content, "发送彩信_制作彩信文字", content)
        self.input_text(sendMakeMms.mms_upload, "发送彩信_制作彩信上传本地文件", imgs)
    # 点击本地上传按钮
    def send_load(self):
        self.click_element(sendMakeMms.mms_upload, "发送彩信_制作彩信本地上传")

    # 点击立即保存
    def send_save(self):
        self.click_element(sendMakeMms.mms_save, "发送彩信_制作彩信立即保存")

    def func_basic(self, data1, data2, data3):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '彩信')
        MenuUtils(self.driver).menu_tab('li', '制作彩信')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_42')  # 获取iframe
        self.send_makeMms(data1, data2, data3)


