# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1
# @Author  : wangyufeng
# @Remark: 直客短信-定时短信
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_msg.timingMsg_page import timingMsgPage as stmp


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
    def test_timingMsg_1_error(self):
        temp = True
        logging.info("*********定时短信——取消按钮，直接点击取消*********")
        temp = stmp(self.driver).func_cancel(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
