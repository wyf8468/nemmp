# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送电子邮件-发送普通邮件
import time
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_email.send_generalEmail_page import SendGemailPage as sgmp
from nmmp_manage.pages.datas.sendEmail_datas import *


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

    def test_sendGeneralEmail_2_success(self):
        logging.info("*********发送邮件：发送普通邮件*********")
        temp = True
        sgmp(self.driver).func_basic(gemail_datas['address'], gemail_datas['name'], gemail_datas['title'], '立即发送',
                                     gemail_datas['time'], gemail_datas['address'],
                                     '提交发送', '确认发送')
        time.sleep(2)
        temp = sgmp(self.driver).func_results('approvalStatusStr', '入库成功', '已发邮件', 'mainFrame_154', 'sendStatusStr',
                                              'returnMsg', "提交成功")
        # 断言判断与预期是否
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
