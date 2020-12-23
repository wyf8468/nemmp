# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : wangyufeng
# @Remark: 电子邮件-制作邮件模板
import time
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.datas.sendEmail_datas import *
from nmmp_manage.pages.logic.send_email.makeEmail_page import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    # @unittest.skip('制作邮件模板用例无条件跳过')
    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    @unittest.skip('制作普通邮件模板用例无条件跳过')
    def test_makeEmail_1_success(self):
        logging.info("*********制作电子邮件模板用例：普通邮件模板*********")
        title = makemailPage(self.driver).func_basic('普通邮件', makeVideo_datas['title'], makeVideo_datas['content'])
        print(title)
        self.driver.implicitly_wait(2)

    @unittest.skip('制作个性邮件模板用例无条件跳过')
    def test_makeEmail_2_success(self):
        logging.info("*********制作电子邮件模板用例：个性邮件模板*********")
        title = makemailPage(self.driver).func_basic('个性邮件', makeVideo_datas['title'], makeVideo_datas['content'])
        print(title)
        self.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
