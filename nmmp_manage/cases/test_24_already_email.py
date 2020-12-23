# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : wangyufeng
# @Remark: 电子邮件-已发邮件用例
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_email.alreadyEmail_page import alreadyEmailPage as adep


@ddt.ddt
class TestLogin(unittest.TestCase):

    # @unittest.skip('短信审核箱')
    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 异常用例
    # @unittest.skip('已发邮件-预览')
    def test_alreadyEmail_1_error(self):
        temp = True
        logging.info("*********已发邮件——预览，直接点击*********")
        temp = adep(self.driver).func_preview(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('已发邮件-重新发送')
    def test_alreadyEmail_2_error(self):
        temp = True
        logging.info("*********已发邮件——重新发送，直接点击*********")
        temp = adep(self.driver).func_alterSend(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('已发邮件-软退一键重发')
    def test_alreadyEmail_3_error(self):
        temp = True
        logging.info("*********已发邮件——软退一键重发，直接点击*********")
        temp = adep(self.driver).func_keyResend(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)
    # @unittest.skip('已发邮件-导出')

    def test_alreadyEmail_4_error(self):
        temp = True
        logging.info("*********已发邮件——导出，直接点击*********")
        temp = adep(self.driver).func_derive(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
