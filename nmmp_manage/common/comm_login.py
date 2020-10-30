# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/07
# @Author  : wangyufeng
# @Remark: 封装公共登录
from nmmp_manage.pages.element.index.login_locator import LoginPageLocator as lpl
from nmmp_manage.pages.logic.index.login_page import LoginPage
# from nmmp_manage.pages.logic.home.home_page import HomePage
from nmmp_manage.pages.datas import login_datas as ld
from nmmp_manage.common.comm_datas import *
import time

class comm_login:

    def __init__(self, driver):
        self.driver = driver

    def Loginfor(self, username, password, code):
        LoginPage(self.driver).login(username, password, code)
        current_url = self.driver.current_url  # 获取当前页面的网址
        urlone = current_url.split('/')
        urlTwo = verify_url.split('/')  # 登录成功后期望的网址
        if urlone[3] == urlTwo[3]:
            pass
        else:
            print(LoginPage(self.driver).get_errorMsg())
            # 断言：判断提示信息是否一致
            self.driver.assertEqual(ld.success_data["check"], LoginPage(self.driver).get_errorMsg())


