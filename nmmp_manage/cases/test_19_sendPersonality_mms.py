# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 发送彩信-制作彩信
import time
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.pages.datas.login_datas import *
from nmmp_manage.common.menuUtils import *
from selenium import webdriver
from nmmp_manage.pages.logic.send_mms.send_personalityMms_page import SendPerMmsPage
from nmmp_manage.pages.datas.sendMms_datas import *



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
    def test_sendMakeMms_2_success(self):
        time.sleep(2)
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '彩信')
        print(111)
        MenuUtils(self.driver).menu_tab('li', '发送个性彩信')
        time.sleep(1)
        comm_frame(self.driver).Frame('mainFrame_1004')  # 获取iframe
        logging.info("*********发送个性彩信用例：正常场景*********")
        SendPerMmsPage(self.driver).send_pMmsUpload(success_pMmsDatas['phone'])
        time.sleep(1)
        SendPerMmsPage(self.driver).send_content(success_pMmsDatas['title'], success_pMmsDatas['content'], success_pMmsDatas['imgs'])
        MenuUtils(self.driver).menu_tab('li', '姓名')
        time.sleep(1)
        SendPerMmsPage(self.driver).send_submit()
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_toSendYlan')  # 获取iframe
        SendPerMmsPage(self.driver).send_promptly()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
