# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 发送个性彩信
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_mms.send_personalityMms_locator import SendPersoalitynMmsLocator as sendpMms


class SendPerMmsPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    # 导入收件号码
    def send_pMmsUpload(self, phone):
        self.input_text(sendpMms.phone_upload, "发送个性彩信_导入收件号码", phone)
        self.click_element(sendpMms.file_upload, "发送个性彩信_导入")

    # 输入标题内容
    def send_content(self, title, content, images):
        self.input_text(sendpMms.mms_title, "发送个性彩信_彩信标题", title)
        self.input_text(sendpMms.mms_content, "发送个性彩信_彩信文字", content)
        self.input_text(sendpMms.images_upload, "发送彩信_制作彩信本地上传", images)
        self.click_element(sendpMms.inset_variable, "发送个性彩信_插入变量")

    # 点击预处理
    def send_submit(self):
        self.click_element(sendpMms.mms_pretreatment, "发送个性彩信_预处理")

    # 点击立即发送
    def send_promptly(self):
        self.click_element(sendpMms.promptly_send, "发送个性彩信_立即发送")

