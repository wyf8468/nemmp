# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/07
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-立即发送成功
import time
import unittest
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
from nmmp_manage.pages.logic.send_msg.send_msg_page import SendMsgPage
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
        logging.info("*********发送普通短信用例：正常场景-提交成功*********")
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_data["phone"], msgDatas.success_data["content"])
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(4)
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认按钮
        time.sleep(2)

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
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        # 断言：判断提示信息是否一致
        self.assertEqual(data["check"], SendMsgPage(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
        """
        verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
        0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
        1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
        2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
        
        """



