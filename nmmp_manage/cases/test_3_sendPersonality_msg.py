# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11
# @Author  : wangyufeng
# @Remark: 发送个性短信基本发送
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.common.comm_timeCompare import date_compare
from nmmp_manage.pages.logic.send_msg.send_personalityMgs_page import SendPerMsgPage as sendPerMsg
from nmmp_manage.common.fileUpload import *
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas


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
    # 立即发送
    def test_sendPerMsg_2_success(self):
        temp = True
        # 选择菜单到发送普通短信页面
        logging.info("*********发送个性短信：正常发送用例*********")
        # 导入收件号码和输入短信内容
        sendPerMsg(self.driver).func_basics(msgDatas.personality_success['filePath'], msgDatas.personality_success['text'], '立即发送', msgDatas.success_data['time'], '确认发送')
        self.driver.implicitly_wait(5)
        sendPerMsg(self.driver).func_results('approvalStatusStr', msgDatas.success_data["checkText"], '已发短信', 'mainFrame_30',   'sendStatus', 'statusCodeCh', 'statusCodeEn', msgDatas.success_data["codeText"])
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # 定时发送
    # @unittest.skip('个性短信下发用例无条件跳过')
    def test_sendPerMsg_3_success(self):
        temp = True
        # 选择菜单到发送普通短信页面
        logging.info("*********发送个性短信：正常发送用例*********")
        # 导入收件号码和输入短信内容
        time_timeing = sendPerMsg(self.driver).func_basics(msgDatas.personality_success['filePath'], msgDatas.personality_success['text'], '定时发送', msgDatas.personality_success['time'], '确认发送')
        self.driver.implicitly_wait(5)
        # 获取当前时间
        flag = date_compare(time_timeing)  # 两个日期进行比较，为真返回True，反之flag
        self.driver.implicitly_wait(5)
        if flag == False:
            temp = sendPerMsg(self.driver).func_results('approvalStatusStr', msgDatas.success_data["checkText"], '已发短信', 'mainFrame_30', 'sendStatus', 'statusCodeCh', 'statusCodeEn',
                                             msgDatas.success_data["codeText"])
        elif flag == True:
            msg_checkTrOne = sendPerMsg(self.driver).func_checkResults('approvalStatusStr')
            self.assertEqual(msgDatas.success_data["checkText1"], msg_checkTrOne.text)
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # 取消发送
    # @unittest.skip('个性短信下发用例无条件跳过')
    def test_sendPerMsg_4_success(self):
        temp = True
        # 选择菜单到发送普通短信页面
        logging.info("*********发送个性短信：正常发送用例*********")
        # 导入收件号码和输入短信内容
        sendPerMsg(self.driver).func_basics(msgDatas.personality_success['filePath'],
                                            msgDatas.personality_success['text'], '立即发送', msgDatas.success_data['time'],
                                            '取消发送')
        # 断言判断与预期是否一致
        self.assertTrue(temp)

    # 异常用例
    def test_sendPerMsg_1_error(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)


