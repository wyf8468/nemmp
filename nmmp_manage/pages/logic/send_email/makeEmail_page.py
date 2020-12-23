# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18
# @Author  : wangyufeng
# @Remark: 制作邮件模板模块封装
from nmmp_manage.common.comm_frame import comm_frame
from nmmp_manage.common.menuUtils import MenuUtils
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.send_email.makeEmail_locator import makemailLocator as smel


class makemailPage(seleniumUtils):
    def __init__(self, driver):
        self.driver = driver

    def func_basic(self, value, title, content):
        # 选择菜单到彩信
        MenuUtils(self.driver).menu_tab('li', '电子邮件')
        MenuUtils(self.driver).menu_tab('li', '邮件模板')
        MenuUtils(self.driver).menu_tab('li', '制作模板')
        comm_frame(self.driver).Frame('mainFrame_101')  # 获取iframe
        self.input_text(smel.memail_tile, '输入模板名称', title)
        self.driver.implicitly_wait(2)
        if value == '普通邮件':
            self.click_element(smel.memail_general, '选择制作普通邮件')
        else:
            self.click_element(smel.memail_personality, '选择制作个性邮件')
            self.click_element(smel.memail_variable, '点击插入的变量')
            MenuUtils(self.driver).menu_tab('li', '全部联系人')
        self.driver.implicitly_wait(2)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        self.input_text(smel.memail_content, '输入邮件内容', content)
        self.driver.switch_to.default_content()  # 释放iframe
        self.driver.implicitly_wait(2)
        comm_frame(self.driver).Frame('mainFrame_101')  # 获取iframe
        self.click_element(smel.memail_save, '点击保存')
        self.driver.implicitly_wait(2)
        return title




