# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/07
# @Author  : wangyufengmeizi
# @Remark: 发送普通短信基本发送-立即发送成功
import unittest
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
from nmmp_manage.pages.logic.send_msg.send_generalMsg_page import SendMsgPage
from nmmp_manage.common.comm_setUpClass import *
from nmmp_manage.common.comm_timeCompare import *
from nmmp_manage.common.comm_frame import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
       csuc = commSetUpClass()
       self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # ------------------------------------------------------------正常用例-------------------------------------------------------------------------------
    # @unittest.skip('普通短信下发用例无条件跳过')
    # 发送普通短信基本发送 - 短信计费验证
    @ddt.data(*msgDatas.billing_datas)
    def test_sendGeneral_2_success(self, data):
        logging.info("*********发送普通短信用例：正常场景-短信计费验证*********")
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_data["phone"], data["content"])

    # @unittest.skip('普通短信下发用例无条件跳过')
    # 发送普通短信基本发送 - 提取号码数验证
    @ddt.data(*msgDatas.extract_phoneNum)
    def test_sendGeneral_3_success(self, data):
        temp = True
        logging.info("*********发送普通短信用例：正常场景-提取号码总数*********")
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        SendMsgPage(self.driver).send_normal_msg(data['phone'], msgDatas.success_data["content"])
        temp = SendMsgPage(self.driver).func_verifyPhone(data["check1"], data["check2"], data["check3"], data["check4"])
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('普通短信下发用例无条件跳过')
    # 发送普通短信基本发送 - 双回T退订提示语验证
    @ddt.data(*msgDatas.data_unreg)
    def test_sendGeneral_4_success(self, data):
        logging.info("*********发送普通短信用例：正常场景-双回T提示语验证*********")
        i = 0
        while i < len(msgDatas.retreatStr):
            print(msgDatas.retreatStr[i])
            SendMsgPage(self.driver).func_doubleBasics(msgDatas.success_data["phone"], data["content"], msgDatas.retreatStr[i])
            # 断言：判断提示信息是否一致
            self.assertEqual(data["check"], SendMsgPage(self.driver).get_popMsg())
            time.sleep(2)
            SendMsgPage(self.driver).send_filedPop()  # 点击弹窗上的关闭按钮
            i = i + 1

    # @unittest.skip('普通短信下发用例无条件跳过')
    # 发送普通短信基本发送 - 开启链接跟踪提示语验证
    def test_sendGeneral_5_success(self):
        logging.info("*********发送普通短信用例：正常场景-开启链接跟踪*********")
        temp = True
        temp = SendMsgPage(self.driver).func_linkBasics(msgDatas.success_linkData["phone"], msgDatas.success_linkData["content"], msgDatas.success_linkData["check1"], msgDatas.success_linkData["check2"])
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认按钮
        time.sleep(4)
        temp = SendMsgPage(self.driver).func_results('approvalStatusStr', msgDatas.success_data["checkText"], '已发短信','mainFrame_30', 'sendStatus', 'statusCodeCh', 'statusCodeEn', msgDatas.success_data["codeText"])
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('普通短信下发用例无条件跳过')
    # 发送普通短信基本发送-点击弹窗上的取消按钮（不发送）
    def test_sendGeneral_6_success(self):
        logging.info("*********发送普通短信用例：正常场景-立即发送取消发送*********")
        SendMsgPage(self.driver).func_basics(msgDatas.success_data["phone"], msgDatas.success_data["content"], msgDatas.success_data["time"], '立即发送')
        time.sleep(2)
        SendMsgPage(self.driver).send_filedPop()  # 点击取消按钮-关闭弹窗且不执行发送操作

    # 发送普通短信基本发送-提交成功
    def test_sendGeneral_7_success(self):
        temp = True
        logging.info("*********发送普通短信用例：正常场景-立即发送提交成功*********")
        SendMsgPage(self.driver).func_basics(msgDatas.success_data["phone"], msgDatas.success_data["content"], msgDatas.success_data["time"], '立即发送')
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认按钮
        time.sleep(4)
        temp = SendMsgPage(self.driver).func_results('approvalStatusStr', msgDatas.success_data["checkText"], '已发短信', 'mainFrame_30',  'sendStatus', 'statusCodeCh', 'statusCodeEn', msgDatas.success_data["codeText"])
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # @unittest.skip('普通短信下发用例无条件跳过')
    # 发送普通短信基本发送 - 定时发送提交成功
    def test_sendGeneral_8_success(self):
        logging.info("*********发送普通短信用例：正常场景-定时发送提交成功*********")
        temp = True
        time_timeing = SendMsgPage(self.driver).func_basics(msgDatas.success_data["phone"], msgDatas.success_data["content"], msgDatas.success_data["time"], '定时发送')
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认按钮
        time.sleep(2)
        # 获取当前时间
        flag = date_compare(time_timeing)  # 两个日期进行比较，为真返回True，反之flag
        time.sleep(2)
        # 定时时间和当前时间进行比较
        if flag == False:
            temp = SendMsgPage(self.driver).func_results('approvalStatusStr', msgDatas.success_data["checkText"], '已发短信', 'mainFrame_30', 'sendStatus', 'statusCodeCh', 'statusCodeEn', msgDatas.success_data["codeText"])
            self.assertTrue(temp)
        elif flag == True:
            msg_checkTrOne = SendMsgPage(self.driver).func_checkResults('approvalStatusStr')
            self.assertEqual(msgDatas.success_data["checkText1"], msg_checkTrOne.text)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # ------------------------------------------------------------异常用例-------------------------------------------------------------------------------
    # @unittest.skip('普通短信下发用例无条件跳过')
    @ddt.data(*msgDatas.wrong_datas)
    def test_sendGeneral_1_error(self, data):
        logging.info("*********发送普通短信用例：异常场景-立即发送提交失败*********")
        SendMsgPage(self.driver).func_basics(data["phone"], data["content"], msgDatas.success_data["time"], '立即发送')
        # 断言 判断提示信息是否一致
        self.assertEqual(data["check"], SendMsgPage(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)



