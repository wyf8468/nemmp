# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : wangyufeng
# @Remark: 视频短信-视频短信审核箱
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_videoMsg.approvaVideoMsg_page import alreadyVideoMsgPage as  avmp


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
    # @unittest.skip('视频短信审核箱-取消按钮')
    def test_alreadyVideoMsg_1_error(self):
        temp = True
        logging.info("*********视频短信审核箱——号码明细，直接点击*********")
        temp = avmp(self.driver).func_phoneDetail(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('视频短信审核箱-预览')
    def test_alreadyVideoMsg_2_error(self):
        temp = True
        logging.info("*********视频短信审核箱——预览，直接点击*********")
        temp = avmp(self.driver).func_preview(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('视频短信审核箱-取消发送')
    def test_alreadyVideoMsg_3_error(self):
        temp = True
        logging.info("*********视频短信审核箱——取消发送，直接点击*********")
        temp = avmp(self.driver).func_cancelSend(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('视频短信审核箱-导出')
    def test_alreadyVideoMsg_4_error(self):
        temp = True
        logging.info("*********视频短信审核箱——导出，直接点击*********")
        temp = avmp(self.driver).func_derive(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
