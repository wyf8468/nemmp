# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15
# @Author  : wangyufeng
# @Remark: 提取字符串中的数字（正则表达式）
import re


class comm_extractDigital:
    def __init__(self, driver):
        self.driver = driver

    def comm_extractDigital(self, string):
        #string = '有小号吗：0'
        verify = re.findall("\d+", string)[0]
        print(verify)
        return verify


