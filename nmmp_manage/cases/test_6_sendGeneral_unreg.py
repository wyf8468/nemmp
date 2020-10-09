# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/08
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-退订设置
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/09
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-短信双回T功能
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

    # 正常用例
    @unittest.skip('用例无条件跳过')
    def test_sendGeneral_2_success(self):
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-双回T提示提交成功*********")
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_unreg["phone"], msgDatas.success_unreg["content"])
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(4)
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认发送按钮
        time.sleep(2)
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认按钮
        time.sleep(2)

    @unittest.skip('用例无条件跳过')
    @ddt.data(*msgDatas.wrong_unreg)
    def test_sendGeneral_1_error(self, data):
        time.sleep(2)
        retreatStr = ["回T退", "回T退订", "TD退订", "回N退订", "退订回T", "退订回D"]
        i = 0
        while i <= 5:
        #for i in range(len(retreatStr)):
            print(retreatStr[i])
            # for j in range(len(data)):
            comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
            # print(data["phone"], data["content"])
            # 判断收件号码方式
            MenuUtils(self.driver).menu_tab('li', '手动输入')
            time.sleep(1)
            logging.info("*********发送普通短信用例：异常场景-双回T提示取消发送*********")
            SendMsgPage(self.driver).send_normal_msg('18588885555', data["content"])
            # print(retreatStr[i])
            time.sleep(1)
            SendMsgPage(self.driver).send_unsubscribe()  # 点击退订设置
            MenuUtils(self.driver).menu_tab('li', retreatStr[i])
            SendMsgPage(self.driver).send_immediately()  # 立即发送
            time.sleep(1)
            SendMsgPage(self.driver).send_submit()  # 提交发送
            self.driver.switch_to.default_content()  # 释放iframe
            # 断言：判断提示信息是否一致
            self.assertEqual(data["check"], SendMsgPage(self.driver).get_popMsg())
            time.sleep(2)
            SendMsgPage(self.driver).send_filedPop()  # 点击弹窗上的关闭按钮
            i = i + 1
            print(i)
            time.sleep(1)

    @classmethod
    def tearDownClass(cls):
       cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)





