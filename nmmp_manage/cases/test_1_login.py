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

    # 正常用例
    def test_login_2_success(self):
        logging.info("*********登录用例：正常场景-登录成功*********")
        # 步骤：登录页面-登录操作
        self.lp.login(ld.success_data["user"], ld.success_data["pwd"])
        time.sleep(3)
        # 断言：首页-【今日事务】这个元素存在
        self.assertTrue(HomePage(self.driver).check_login_ele_exists())

    # 异常用例
    @ddt.data(*ld.wrong_datas)
    def test_login_1_error(self, data):
        time.sleep(2)
        logging.info("*********登录用例：异常场景-登录失败*********")
        self.lp.login(data["user"], data["pwd"])
        time.sleep(2)
        # 断言：判断提示信息是否一致
        self.assertEqual(data["check"], LoginPage(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        # 后置：关闭浏览器
        cls.driver.quit()
