# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 发送彩信-制作彩信
import time
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_mms.makeMms_page import makeMmsPage
from nmmp_manage.pages.datas.sendMms_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @unittest.skip('制作彩信用例无条件跳过')
    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    @unittest.skip('制作彩信用例无条件跳过')
    def test_makeMms_2_success(self):
        logging.info("*********发送彩信用例：制作彩信*********")
        makeMmsPage(self.driver).func_basic(makeMms_data['title'], makeMms_data['content'], makeMms_data['imgs'])
        time.sleep(2)
        makeMmsPage(self.driver).send_save()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
