# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : wangyufeng
# @Remark: 彩信-已发彩信
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_mms.alreadyMms_page import alreadyMmsPage as ldmsp


@ddt.ddt
class TestLogin(unittest.TestCase):

    # @unittest.skip('已发彩信')
    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 异常用例
    # @unittest.skip('已发彩信-彩信预览')
    def test_alreadyMms_1_error(self):
        temp = True
        logging.info("*********已发彩信——彩信预览，直接点击*********")
        temp = ldmsp(self.driver).func_preview(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('已发彩信-导出')
    def test_alreadyMms_2_error(self):
        temp = True
        logging.info("*********已发彩信——导出，直接点击*********")
        temp = ldmsp(self.driver).func_derive(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
