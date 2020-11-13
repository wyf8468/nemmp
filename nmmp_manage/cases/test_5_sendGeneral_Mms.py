# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15
# @Author  : wangyufeng
# @Remark: 发送彩信-发送普通彩信
import datetime
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.common.comm_timeCompare import date_compare
from nmmp_manage.pages.logic.send_mms.send_generalMms_page import SendMmsPage
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

    # 立即发送
    def test_sendGeneralMms_2_success(self):
        logging.info("*********发送彩信用例：发送普通彩信立即发送——确认发送*********")
        temp = True
        SendMmsPage(self.driver).func_basic(makeMms_data['phone'], '立即发送', makeMms_data['time'], '确认发送')
        time.sleep(2)
        temp = SendMmsPage(self.driver).func_results('approvalStatusStr', '入库成功', '已发彩信', 'mainFrame_47', 'statusCodeEn',
                                             "提交")
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('普通彩信下发用例无条件跳过')
    # 定时发送
    def test_sendGeneralMms_3_success(self):
        logging.info("*********发送彩信用例：发送普通彩信定时发送——确认发送*********")
        time_timeing = SendMmsPage(self.driver).func_basic(makeMms_data['phone'], '定时发送', makeMms_data['time'], '确认发送')
        time.sleep(2)
        # 获取当前时间
        flag = date_compare(time_timeing)  # 两个日期进行比较，为真返回True，反之flag
        time.sleep(2)
        if flag == False:
            temp = SendMmsPage(self.driver).func_results('approvalStatusStr', '入库成功', '已发彩信', 'mainFrame_47', 'statusCodeEn',
                                                     "提交成功")
        elif flag == True:
            msg_checkTrOne = SendMmsPage(self.driver).func_checkResults('approvalStatusStr')
            self.assertEqual('审核通过', msg_checkTrOne.text)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # 取消发送
    # @unittest.skip('普通彩信下发用例无条件跳过')
    def test_sendGeneralMms_4_success(self):
        logging.info("*********发送彩信用例：发送普通彩信立即发送——取消发送*********")
        SendMmsPage(self.driver).func_basic(makeMms_data['phone'], '立即发送', makeMms_data['time'], '取消发送')
        time.sleep(2)

    # 异常用例
    def test_sendGeneralMms_1_error(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
