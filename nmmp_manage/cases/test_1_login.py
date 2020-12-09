# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : zhujh
# @Described    : 登录用例
import time
import unittest
from nmmp_manage.pages.logic.index.login_page import LoginPage
from nmmp_manage.pages.datas import login_datas as ld
import logging
import ddt
from selenium import webdriver
from nmmp_manage.common.comm_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    # @unittest.skip('用例无条件跳过')
    def setUpClass(cls):
        # 前置：打开浏览器，登录网页
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(web_login_url)
        cls.driver.implicitly_wait(5)  # 隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    # @unittest.skip('用例无条件跳过')
    def test_login_2_success(self):
        logging.info("*********登录用例：正常场景-登录成功*********")
        # 步骤：登录页面-登录操作
        LoginPage(self.driver).login(ld.success_data["user"], ld.success_data["pwd"], ld.success_data['rand'])
        current_url = self.driver.current_url  # 获取当前页面的网址
        urlone = current_url.split('/')
        urlTwo = verify_url.split('/')  # 登录成功后期望的网址
        if urlone[3] == urlTwo[3]:
            pass
        else:
            print(LoginPage(self.driver).get_errorMsg())
            # 断言：判断提示信息是否一致
            self.assertEqual(ld.success_data["check"], LoginPage(self.driver).get_errorMsg())

    # 异常用例
    # @unittest.skip('用例无条件跳过')
    @ddt.data(*ld.wrong_datas)
    def test_login_1_error(self, data):
        time.sleep(2)
        logging.info("*********登录用例：异常场景-登录失败*********")
        LoginPage(self.driver).login(data["user"], data["pwd"], data['rand'])
        time.sleep(2)
        # 断言：判断提示信息是否一致
        self.assertEqual(data["check"], LoginPage(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        # 后置：关闭浏览器
        cls.driver.quit()


