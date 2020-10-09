# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/09
# @Author  : wangyufeng
# @Remark: 获取属性


class getProperty(object):
    def __init__(self, driver):
        self.driver = driver

    def get_pro(self, value, property):
        value.find_element_by_name(property)
        return value.find_element_by_name(property)

