# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11
# @Author  : wangyufeng
# @Remark: 发送个性短信基本发送
import time
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.pages.datas.login_datas import *
from nmmp_manage.common.menuUtils import *
from selenium import webdriver
from nmmp_manage.pages.logic.send_msg.send_personalityMgs_page import SendPerMsgPage as sendPerMsg
from nmmp_manage.common.fileUpload import *
from nmmp_manage.pages.datas import sendMsg_datas as msg


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(web_login_url)
        cls.driver.implicitly_wait(5)  # 隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时
        # 先登录
        comm_login(cls.driver).Loginfor(success_data['user'], success_data['pwd'], "1111")

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    def test_sendGeneral_2_success(self):
        time.sleep(2)
        # 选择菜单到发送普通短信页面
        MenuUtils(self.driver).menu_tab('li', '发送个性短信')
        time.sleep(1)
        comm_frame(self.driver).Frame('mainFrame_27')  # 获取iframe
        # 判断收件号码方式
        # MenuUtils(self.driver).menu_tab('li', '文件导入')
        sendPerMsg(self.driver).send_lead()
        logging.info("*********发送个性短信：正常发送用例*********")
        UpLoad_File(msg.personality_success['filePath'])
        sendPerMsg(self.driver).send_personality_msg(msg.personality_success['text'])
        time.sleep(1)
        self.driver.switch_to.default_content()  # 释放iframe
        sendPerMsg(self.driver).send_affirm()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)


