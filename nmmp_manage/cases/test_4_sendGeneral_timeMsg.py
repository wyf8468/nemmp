# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/08
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-定时发送发送成功
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
    @unittest.skip('用例 1 无条件跳过')
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

    @unittest.skip('用例 1 无条件跳过')
    def test_sendGeneral_2_success(self):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-定时发送提交成功*********")
        # 判断收件号码方式
        MenuUtils(self.driver).menu_tab('li', '手动输入')
        time.sleep(2)
        # 输入收件号码和短信内容
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_timeingData["phone"], msgDatas.success_timeingData["content"])
        # 定时发送
        SendMsgPage(self.driver).send_timeingMode()
        #  输入定时时间
        SendMsgPage(self.driver).send_normal_timeing(msgDatas.success_timeingData['time'])
        # 提交发送
        SendMsgPage(self.driver).send_submit()
        # 释放iframe
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 点击确认按钮-发送成功
        SendMsgPage(self.driver).send_suceedPop()
        time.sleep(2)

    # 异常用例
    @unittest.skip('用例 1 无条件跳过')
    @ddt.data(*msgDatas.wrong_timeingData)
    def test_sendGeneral_1_error(self, data):
        # 获取iframe
        comm_frame(self.driver).Frame('mainFrame_26')
        # 判断收件号码方式
        MenuUtils(self.driver).menu_tab('li', '手动输入')
        time.sleep(2)
        logging.info("*********发送普通短信用例：异常场景-定时发送提交失败*********")
        # 输入收件号码和短信内容
        SendMsgPage(self.driver).send_normal_msg(msgDatas.wrong_timeingData["phone"], msgDatas.wrong_timeingData["content"])
        # SendMsgPage(self.driver).send_normal_msg(data["phone"], data["content"])
        # 定时发送
        SendMsgPage(self.driver).send_timeingMode()
        # 选择定时时间
        SendMsgPage(self.driver).send_normal_timeing(msgDatas.wrong_timeingData["time"])
        # 提交发送
        SendMsgPage(self.driver).send_submit()
        # 释放iframe
        self.driver.switch_to.default_content()
        time.sleep(2)
        # 断言：判断提示信息是否一致
        # self.assertEqual(data["check"], SendMsgPage(self.driver).get_errorMsg())
        self.assertEqual(msgDatas.wrong_timeingData["check"], SendMsgPage(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)




