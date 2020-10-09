# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : zhujh
# @Described    : 登录用例
import time
import unittest
from nmmp_manage.pages.logic.index.login_page import LoginPage
# from nmmp_manage.pages.logic.home.home_page import HomePage
from nmmp_manage.pages.datas import login_datas as ld
import logging
import ddt
from selenium import webdriver
from nmmp_manage.common.comm_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    @unittest.skip('用例无条件跳过')
    def setUpClass(cls):
        # 前置：打开浏览器，登录网页
        #self.driver = webdriver.Chrome(r"D:\files\project\nemmp\nmmp_libs\chromedriver.exe")
        #self .driver.maximize_window()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(web_login_url)
        cls.driver.implicitly_wait(5)  # 隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时

    # 刷新一下当前页面
    #def tearDown(self):
        #self.driver.refresh()

    # 正常用例
    @unittest.skip('用例无条件跳过')
    def test_login_2_success(self):

        logging.info("*********登录用例：正常场景-登录成功*********")
        # 步骤：登录页面-登录操作
        LoginPage(self.driver).login(ld.success_data["user"], ld.success_data["pwd"], ld.success_data['rand'])
        time.sleep(3)
        # 断言：首页-【今日事务】这个元素存在
        # self.assertTrue(HomePage(self.driver).check_login_ele_exists())

    # 异常用例
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


