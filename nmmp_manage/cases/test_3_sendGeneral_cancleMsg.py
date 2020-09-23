# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/08
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-点击弹窗上的取消按钮（不发送）
import time
import unittest
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
from nmmp_manage.pages.logic.send_msg.send_generalMsg_page import SendMsgPage
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.pages.datas.login_datas import *
from nmmp_manage.common.menuUtils import *


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

    def test_sendGeneral_2_success(self):

        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-取消成功*********")
        # 判断收件号码方式
        MenuUtils(self.driver).menu_tab('li', '手动输入')
        time.sleep(2)
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_data["phone"], msgDatas.success_data["content"])
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(4)
        SendMsgPage(self.driver).send_filedPop()  # 点击取消按钮-关闭弹窗且不执行发送操作
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)




