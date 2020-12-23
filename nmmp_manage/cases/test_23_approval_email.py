# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : wangyufeng
# @Remark: 电子邮件-邮件审核箱
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_email.approvalEmail_page import approvalEmailPage as aep


@ddt.ddt
class TestLogin(unittest.TestCase):

    # @unittest.skip('邮件审核箱')
    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 异常用例
    # @unittest.skip('邮件审核箱-修改重发')
    def test_approvalEmail_1_error(self):
        temp = True
        logging.info("*********邮件审核箱——修改重发，直接点击*********")
        temp = aep(self.driver).func_alterRetry(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('邮件审核箱-取消')
    def test_approvalEmail_2_error(self):
        temp = True
        logging.info("*********邮件审核箱——取消，直接点击*********")
        temp = aep(self.driver).func_cancel(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('邮件审核箱-邮址明细')
    def test_approvalEmail_3_error(self):
        temp = True
        logging.info("*********邮件审核箱——邮址明细，直接点击*********")
        temp = aep(self.driver).func_Detail(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('邮件审核箱-附件下载')
    def test_approvalEmail_4_error(self):
        temp = True
        logging.info("*********邮件审核箱——附件下载，直接点击*********")
        temp = aep(self.driver).func_upDown(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('邮件审核箱-预览')
    def test_approvalEmail_5_error(self):
        temp = True
        logging.info("*********邮件审核箱——预览，直接点击*********")
        temp = aep(self.driver).func_preview(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('邮件审核箱-导出')
    def test_approvalEmail_6_error(self):
        temp = True
        logging.info("*********邮件审核箱——导出，直接点击*********")
        temp = aep(self.driver).func_derive(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
