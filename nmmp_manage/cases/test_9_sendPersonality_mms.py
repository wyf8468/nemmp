# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23
# @Author  : wangyufeng
# @Remark: 彩信-发送个性彩信
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_mms.send_personalityMms_page import SendPerMmsPage
from nmmp_manage.pages.datas.sendMms_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    def test_sendPersonMms_2_success(self):
        logging.info("*********发送个性彩信用例：正常场景*********")
        temp = True
        SendPerMmsPage(self.driver).func_basic(success_pMmsDatas['phone'], success_pMmsDatas['title'],
                                               success_pMmsDatas['content'], success_pMmsDatas['imgs'])
        SendPerMmsPage(self.driver).send_submit()
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        comm_frame(self.driver).Frame('mainFrame_toSendYlan')  # 获取iframe
        time.sleep(2)
        SendPerMmsPage(self.driver).send_promptly()
        time.sleep(4)
        temp = SendPerMmsPage(self.driver).func_results('approvalStatusStr', '入库成功', '已发彩信', 'mainFrame_47',
                                                     'statusCodeEn',
                                                     "提交成功")
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
