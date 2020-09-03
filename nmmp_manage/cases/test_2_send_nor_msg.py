# --^_^-- coding:utf-8 --^_^--
# @Remark:测试登录功能

import unittest
from selenium import webdriver
from nmmp_manage.pages.logic.index.login_page import LoginPage
from nmmp_manage.pages.logic.home.home_page import HomePage
from nmmp_manage.pages.datas import login_datas as ld
from nmmp_manage.common import comm_datas as cd
import logging
import ddt
import time


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 前置：打开浏览器，登录网页
        cls.driver = webdriver.Chrome(r"C:\Users\Administrator\PycharmProjects\nemmp\nmmp_libs\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get(cd.web_login_url)
        cls.lp = LoginPage(cls.driver)

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()


    def succcess_s(self):

        send_normal_msg(111,2,2,"dd")

    def fail_s(self):
        send_normal_msg(111, 2, 2,   "sdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
