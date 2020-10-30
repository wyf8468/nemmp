# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 发送电子邮件-发送个性邮件
import time
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.datas.login_datas import *
from nmmp_manage.common.menuUtils import *
from selenium import webdriver
from nmmp_manage.pages.logic.send_email.send_personalityEmail_page import SendPemailPage as spmp
from nmmp_manage.pages.datas.sendEmail_datas import *

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    def test_sendMakeMms_2_success(self):
        logging.info("*********发送个性邮件：正常场景*********")
        spmp(self.driver).func_basic(success_pemailDatas['address'], success_pemailDatas['name'], success_pemailDatas['title'])
        spmp(self.driver).send_affirm()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
