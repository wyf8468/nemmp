# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/09
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-退订设置
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/09
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-链接跟踪
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
    def test_sendGeneral_2_success(self):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-开启链接跟踪提交成功*********")
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_linkData["phone"], msgDatas.success_linkData["content"])
        SendMsgPage(self.driver).send_link()
        # 选择开启链接跟踪
        MenuUtils(self.driver).menu_tab('li', '开启')
        self.driver.switch_to.default_content()  # 释放iframe
        SendMsgPage(self.driver).send_closeLink()   # 关闭链接跟踪弹窗
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认发送按钮
        time.sleep(2)
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认按钮
        time.sleep(1)

    @ddt.data(*msgDatas.wrong_linkData)
    def test_sendGeneral_1_error(self, data):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-开启链接跟踪取消发送*********")
        SendMsgPage(self.driver).send_normal_msg(data["phone"], data["content"])
        SendMsgPage(self.driver).send_link()  # 点击链接跟踪
        # 选择开启链接跟踪
        MenuUtils(self.driver).menu_tab('li', '开启')
        # self.assertEqual(data["check"], SendMsgPage(self.driver).get_errorMsg())
        self.driver.switch_to.default_content()  # 释放iframe
        # 断言：判断提示信息是否一致
        # self.assertEqual(data["check1"], SendMsgPage(self.driver).get_popMsg())
        SendMsgPage(self.driver).send_closeLink()  # 关闭链接跟踪弹窗
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        time.sleep(2)
        self.driver.switch_to.default_content()  # 释放iframe
        SendMsgPage(self.driver).send_filedPop()  # 点击弹窗上的确认发送按钮
        time.sleep(1)
        # 断言：判断提示信息是否一致
        # self.assertEqual(data["check"], SendMsgPage(self.driver).get_popMsg())

    @classmethod
    def tearDownClass(cls):
       cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)





