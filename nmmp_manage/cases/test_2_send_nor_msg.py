# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/04
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送

import unittest

from driver import driver
from selenium import webdriver
from nmmp_manage.pages.logic.home.home_page import HomePage
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
import time
from nmmp_manage.pages.logic.send_msg.send_msg_page import SendMsgPage


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 前置：打开浏览器，登录网页
        cls.driver = webdriver.Chrome(r"D:\files\project\nemmp\nmmp_libs\chromedriver.exe")
        cls.sm = SendMsgPage(cls.driver)

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

        # 正常用例
    def test_login_2_success(self):
        logging.info("*********发送普通短信用例：正常场景-提交成功*********")
        # 步骤：发送普通短信页面-登录操作
        self.driver.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/ul/li[1]').click()
        self.sm.send_normal_msg(msgDatas.success_data["phone"], msgDatas.success_data["content"])
        time.sleep(3)
        # 断言：首页 -【今日事务】这个元素存在
        self.assertTrue(HomePage(self.driver).check_login_ele_exists())


    # 异常用例
    @ddt.data(*msgDatas.wrong_datas)
    def test_login_1_error(self, data):
        time.sleep(2)
        logging.info("*********发送普通短信用例：异常场景-提交失败*********")
        self.sm.send_normal_msg(data["phone"], data["content"])
        time.sleep(2)
        # 断言：判断提示信息是否一致
        self.assertEqual(msgDatas.success_data["check"], self.sm(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        # 后置：关闭浏览器
        cls.driver.quit()



