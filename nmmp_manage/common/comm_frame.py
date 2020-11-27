# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/08
# @Author  : wangyufeng
# @Remark: 封装公共获取iframe

class comm_frame:

    def __init__(self, driver):
        self.driver = driver
    # 定义登陆函数，将登陆作为公共调用的模块，进行数据传递,因此不需要导入webdriver这个模块

    def Frame(self,  frame):
        # 登录后的
        self.driver.switch_to_frame(self.driver.find_element_by_id(frame))  # 获取当前frame
