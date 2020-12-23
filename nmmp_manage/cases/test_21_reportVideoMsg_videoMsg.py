# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : wangyufeng
# @Remark: 视频短信-视频短信审核箱
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_videoMsg.reportVideoMsg_page import reportVideoMsgPage as  rvmp


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
    # @unittest.skip('模板报备中心-编辑')
    def test_reportVideoMsg_1_error(self):
        temp = True
        logging.info("*********模板报备中心——编辑，直接点击*********")
        temp = rvmp(self.driver).func_compile(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('模板报备中心-删除')
    def test_reportVideoMsg_2_error(self):
        temp = True
        logging.info("*********模板报备中心——删除，直接点击*********")
        temp = rvmp(self.driver).func_delete(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('模板报备中心-取消')
    def test_reportVideoMsg_3_error(self):
        temp = True
        logging.info("*********模板报备中心——取消，直接点击*********")
        temp = rvmp(self.driver).func_cancel(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('模板报备中心-提交审核')
    def test_reportVideoMsg_4_error(self):
        temp = True
        logging.info("*********模板报备中心——提交审核，直接点击*********")
        temp = rvmp(self.driver).func_audit(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('模板报备中心-导出')
    def test_reportVideoMsg_5_error(self):
        temp = True
        logging.info("*********模板报备中心——导出，直接点击*********")
        temp = rvmp(self.driver).func_derive(0)
        # print(temp)
        self.driver.implicitly_wait(2)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
