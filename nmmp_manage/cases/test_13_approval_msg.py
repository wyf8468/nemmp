# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1
# @Author  : wangyufeng
# @Remark: 直客短信-短信审核箱
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_msg.approvalMsg_page import approvalMsgPage as samp


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

    # 正常用例
    # @unittest.skip('短信审核箱-取消按钮')
    def test_approvalMsg_1_error(self):
        temp = True
        logging.info("*********短信审核箱——取消按钮，直接点击取消*********")
        temp = samp(self.driver).func_cancel(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('短信审核箱-修改重发')
    def test_approvalMsg_2_error(self):
        temp = True
        logging.info("*********短信审核箱——修改重发，直接点击修改重发*********")
        temp = samp(self.driver).func_alterRetry(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('短信审核箱-号码明细')
    def test_approvalMsg_3_error(self):
        temp = True
        logging.info("*********短信审核箱——号码明细，直接点击号码明细*********")
        temp = samp(self.driver).func_phoneDetail(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('短信审核箱-导出当前页选中的记录')
    def test_approvalMsg_4_error(self):
        temp = True
        logging.info("*********短信审核箱——导出，直接导出当前页选中数据*********")
        temp = samp(self.driver).func_derive(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
