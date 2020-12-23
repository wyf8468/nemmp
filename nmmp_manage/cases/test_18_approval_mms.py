# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16
# @Author  : wangyufeng
# @Remark: 彩信-彩信审核箱
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_mms.approvalMms_page import productsMmsPage as pmmsp


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
    # @unittest.skip('平台审核箱-取消按钮')
    def test_approvalMms_1_error(self):
        temp = True
        logging.info("*********平台彩信审核箱——取消按钮，直接点击取消*********")
        temp = pmmsp(self.driver).func_cancel(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('平台审核箱-修改重发按钮')
    def test_approvalMms_2_error(self):
        temp = True
        logging.info("*********平台彩信审核箱——修改重发按钮，直接点击修改重发*********")
        temp = pmmsp(self.driver).func_againSend(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('平台审核箱-号码明细按钮')
    def test_approvalMms_3_error(self):
        temp = True
        logging.info("*********平台彩信审核箱——号码明细按钮，直接点击号码明细*********")
        temp = pmmsp(self.driver).func_detail(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('平台审核箱-彩信预览按钮')
    def test_approvalMms_4_error(self):
        temp = True
        logging.info("*********平台彩信审核箱——彩信预览按钮，直接点击彩信预览*********")
        temp = pmmsp(self.driver).func_preview(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('平台审核箱-导出')
    def test_approvalMms_5_error(self):
        temp = True
        logging.info("*********平台彩信审核箱——彩信预览按钮，直接点击导出*********")
        temp = pmmsp(self.driver).func_derive(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
