# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  : wangyufeng
# @Remark: 直客短信-已发短信
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_msg.alreadyMsg_page import approvalMsgPage as amp


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
    # @unittest.skip('已发短信-编辑重发')
    def test_alreadyMsg_1_error(self):
        temp = True
        logging.info("*********已发短信——编辑重发按钮，直接点击编辑重发*********")
        temp = amp(self.driver).func_editSend(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('已发短信-时间段导出')
    def test_alreadyMsg_2_error(self):
        temp = True
        logging.info("*********已发短信——时间段导出按钮，直接点击取消*********")
        temp = amp(self.driver).func_timeDerive(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('已发短信-导出')
    def test_alreadyMsg_3_error(self):
        temp = True
        logging.info("*********已发短信——导出，直接点击导出（导出全部）*********")
        temp = amp(self.driver).func_derive(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
