# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/28
# @Author  : wangyufeng
# @Remark: 封装公共移除输入框属性readonly

class comm_readonly:

    def __init__(self, driver):
        self.driver = driver

    def readonly(self,  data):
        js = 'document.getElementById("'+data+'").removeAttribute("readonly")'
        self.driver.execute_script(js)
