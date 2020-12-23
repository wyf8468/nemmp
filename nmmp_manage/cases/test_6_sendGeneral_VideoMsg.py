# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17
# @Author  : wangyufeng
# @Remark: 发送视频短信-发送普通视频短信
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.common.comm_timeCompare import date_compare
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_manage.pages.logic.send_videoMsg.send_generalVideoMsg_page import SendVedioMsgPage as svmp
from nmmp_manage.pages.datas.sendVideoMsg_datas import *

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

    def test_sendVideoMsg_2_success(self):
        temp = True
        logging.info("*********发送视频短信用例：发送普通视频短信*********")
        svmp(self.driver).func_basic(suceess_datas['phone'], '立即发送', suceess_datas['time'], '确认发送')
        self.driver.implicitly_wait(5)
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '视频短信')
        MenuUtils(self.driver).menu_tab('li', '视频短信审核箱')
        time.sleep(2)
        temp = svmp(self.driver).func_results('approvalStatusStr', '入库成功', '已发视频短信', 'mainFrame_1888', 'statusCode', 'remark','提交失败')
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @unittest.skip('用例无条件跳过')
    def test_sendVideoMsg_3_success(self):
        logging.info("*********发送视频短信用例：发送普通视频短信-定时发送*********")
        temp = True
        time_timeing = svmp(self.driver).func_basic(suceess_datas['phone'], '定时发送', suceess_datas['time'], '确认发送')
        # 获取当前时间
        flag = date_compare(time_timeing)  # 两个日期进行比较，为真返回True，反之flag
        self.driver.implicitly_wait(5)
        if flag == False:
            temp = svmp(self.driver).func_results('approvalStatusStr', '入库成功', '已发视频短信',
                                                  'mainFrame_1888', 'statusCode', 'remark',
                                                  '提交成功')

        else:
            msg_checkTrOne = svmp(self.driver).func_checkResults('approvalStatusStr')
            self.assertEqual('审核通过', msg_checkTrOne.text)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
