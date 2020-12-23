# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12
# @Author  : wangyufeng
# @Remark: 彩信-彩信产品
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_mms.productsMms_page import productsMmsPage as pmmsp


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 异常用例
    # @unittest.skip('彩信-制作彩信')
    def test_productsMms_1_error(self):
        temp = True
        logging.info("*********彩信——制作彩信按钮，直接点击制作彩信*********")
        temp = pmmsp(self.driver).func_make(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('彩信-修改')
    def test_productsMms_2_error(self):
        temp = True
        logging.info("*********彩信——修改，直接点击修改*********")
        temp = pmmsp(self.driver).func_modification(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('彩信-预览')
    def test_productsMms_3_error(self):
        temp = True
        logging.info("*********彩信——预览，直接点击预览*********")
        temp = pmmsp(self.driver).func_preview(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('彩信-预览')
    def test_productsMms_4_error(self):
        temp = True
        logging.info("*********彩信——删除，直接点击删除*********")
        temp = pmmsp(self.driver).func_delete(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
