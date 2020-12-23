# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送生日短信-发送生日短信用例
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_msg.send_birthdayMsg_page import SendBirthMsgPage as sbmp
from nmmp_manage.common.fileUpload import *
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import xlrd
import datetime
from nmmp_manage.common.editfiles import editFiles


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
    def test_sendBirthMsg_2_success(self):
        logging.info("*********发送生日短信：发送生日短信正常用例*********")
        sbmp(self.driver).func_basic(msgDatas.birthday_success['filePath'], msgDatas.birthday_success['content'], msgDatas.birthday_success['days'],
                                      msgDatas.birthday_success['hour'], msgDatas.birthday_success['imune'])
        sbmp(self.driver).send_affirm()
        self.driver.implicitly_wait(5)

        # 读取excel文档
        tables = editFiles(self.driver).edit_file(msgDatas.birthday_success['filePath'], 0)
        # 将第二行第二列日期转化为标准日期格式；
        birthTime = xlrd.xldate_as_datetime(tables.cell(1, 2).value, 0)
        print(birthTime)
        # 提取日期时间中的日期
        birthTime_new = datetime.datetime.strptime(str(birthTime), '%Y-%m-%d %H:%M:%S').date()
        print(birthTime_new)

        self.driver.implicitly_wait(5)
        #temp = sbmp(self.driver).func_results('approvalStatusStr', '审核通过', '已发短信',
                                                     #'mainFrame_30', 'sendStatus', 'statusCodeCh', 'statusCodeEn',
                                                    #msgDatas.success_data["codeText"])
        msg_checkTrOne = sbmp(self.driver).func_checkResults('approvalStatusStr')
        self.assertEqual(msgDatas.success_data["checkText1"], msg_checkTrOne.text)

        # 断言判断与预期是否一致
        #self.assertTrue(temp)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)


