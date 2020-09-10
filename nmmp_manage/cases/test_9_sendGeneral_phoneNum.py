# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/09
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-提取号码总数
import time
import unittest
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
from nmmp_manage.pages.logic.send_msg.send_msg_page import SendMsgPage
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.pages.datas.login_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(web_login_url)
        cls.driver.implicitly_wait(5)  # 隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时
        # 先登录
        comm_login(cls.driver).Loginfor(success_data['user'], success_data['pwd'], "1111")

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    @ddt.data(*msgDatas.extract_phoneNum)
    def test_sendGeneral_2_success(self, data):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-开启链接跟踪提交成功*********")
        SendMsgPage(self.driver).send_normal_msg(data['phone'], '节日快乐')
        # 断言 判断计费条数是否一致
        self.assertEqual(data["check"], SendMsgPage(self.driver).get_phoneNum())
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)

