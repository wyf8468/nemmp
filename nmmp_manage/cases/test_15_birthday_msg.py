# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10
# @Author  : wangyufeng
# @Remark: 直客短信-生日短信
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_msg.birthdayMsg_page import birthdayMsgPage


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
    # @unittest.skip('生日短信-查看详情')
    def test_birthdayMsg_1_error(self):
        temp = True
        logging.info("*********生日短信——查看详情按钮，直接点击查看详情*********")
        temp = birthdayMsgPage(self.driver).func_details(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('生日短信-取消发送')
    def test_birthdayMsg_2_error(self):
        temp = True
        logging.info("*********生日短信——取消发送按钮，直接点击取消发送*********")
        temp = birthdayMsgPage(self.driver).func_cancel(0)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
