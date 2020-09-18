# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 发送生日短信-发送生日短信用例
import time
import unittest
import logging
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.common.comm_frame import *
from nmmp_manage.pages.datas.login_datas import *
from nmmp_manage.common.menuUtils import *
from selenium import webdriver
from nmmp_manage.pages.logic.send_msg.send_birthdayMsg_page import SendBirthMsgPage as sbmp
from nmmp_manage.common.fileUpload import *
from nmmp_manage.pages.datas import sendMsg_datas as msg

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
    def test_sendBirthMsg_2_success(self):
        time.sleep(2)
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '直客短信')
        print(111)
        MenuUtils(self.driver).menu_tab('li', '发送生日短信')
        time.sleep(1)
        comm_frame(self.driver).Frame('mainFrame_353')  # 获取iframe
        logging.info("*********发送生日短信：发送生日短信正常用例*********")
        sbmp(self.driver).send_upload()
        UpLoad_File(msg.birthday_success['filePath'])
        time.sleep(1)
        sbmp(self.driver).send_birthday_msg(msg.birthday_success['content'])
        MenuUtils(self.driver).menu_tab('li', msg.birthday_success['days'])
        sbmp(self.driver).send_hour()
        MenuUtils(self.driver).menu_tab('li', msg.birthday_success['hour'])
        sbmp(self.driver).send_minute()
        MenuUtils(self.driver).menu_tab('li', msg.birthday_success['imune'])
        sbmp(self.driver).send_dispose()
        self.driver.switch_to.default_content()  # 释放iframe
        sbmp(self.driver).send_affirm()
        time.sleep(1)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
