# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/08
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-清除收件号码
import time
import unittest
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
from nmmp_manage.pages.logic.send_msg.send_generalMsg_page import SendMsgPage
from nmmp_manage.common.menuUtils import *
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.pages.datas.login_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @unittest.skip('用例无条件跳过')
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

    @unittest.skip('用例无条件跳过')
    # 正常用例
    def test_sendGeneral_2_success(self):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-清除成功*********")
        # 判断收件号码方式
        MenuUtils(self.driver).menu_tab('li', '手动输入')
        time.sleep(1)
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_clearPhone["phone"], msgDatas.success_clearPhone["content"])
        MenuUtils(self.driver).menu_tab('a', '清除移动')
        time.sleep(1)
        MenuUtils(self.driver).menu_tab('a', '清除联通')
        time.sleep(1)
        MenuUtils(self.driver).menu_tab('a', '清除电信')
        time.sleep(1)
        MenuUtils(self.driver).menu_tab('a', '清除港澳台')
        time.sleep(1)
        MenuUtils(self.driver).menu_tab('a', '清除所有')

    @unittest.skip('用例无条件跳过')
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
"""
    # 异常用例
    @ddt.data(*msgDatas.wrong_datas)
    def test_sendGeneral_1_error(self, data):
        # 获取iframe
        comm_frame(self.driver).Frame('mainFrame_26')
        # 选择菜单到发送普通短信页面
        MenuUtils(self.driver).menu_tab('li', '发送普通短信')
        time.sleep(2)
        # 判断收件号码方式
        MenuUtils(self.driver).menu_tab('li', '手动输入')
        time.sleep(2)
        logging.info("*********发送普通短信用例：异常场景-提交失败*********")
        SendMsgPage(self.driver).send_normal_msg(data["phone"], data["content"])
        MenuUtils(self.driver).menu_tab('a', '清除移动')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)

"""


