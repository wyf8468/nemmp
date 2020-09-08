# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/04
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送

import unittest
from nmmp_manage.pages.logic.home.home_page import HomePage
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
from nmmp_manage.pages.logic.send_msg.send_msg_page import SendMsgPage
from nmmp_manage.common.menuUtils import *
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *


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
    def test_sendNorMsg_2_success(self):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-提交成功*********")
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_data["phone"], msgDatas.success_data["content"])
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(3)
        SendMsgPage(self.driver).send_suceedPop()
        time.sleep(3)

    # 异常用例
    @ddt.data(*msgDatas.wrong_datas)
    def test_sendNorMsg_1_error(self, data):
        # 获取iframe
        comm_frame(self.driver).Frame('mainFrame_26')
        # 选择菜单到发送普通短信页面
        MenuUtils(self.driver).menu_tab('发送普通短信')
        time.sleep(2)
        # 判断收件号码方式
        MenuUtils(self.driver).menu_tab('手动输入')
        time.sleep(2)
        logging.info("*********发送普通短信用例：异常场景-提交失败*********")
        SendMsgPage(self.driver).send_normal_msg(data["phone"], data["content"])
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        # 断言：判断提示信息是否一致
        self.assertEqual(data["check"], SendMsgPage(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        # pass
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)



