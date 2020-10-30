#!/usr/bin/env python
# coding=utf-8

import xlrd


class editFiles:
    def __init__(self, driver):
        self.driver = driver
    def edit_file(self, file, n):

        # data = xlrd.open_workbook(msgDatas.birthday_success['filePath'])
        data = xlrd.open_workbook(file)
        # 查看工作表
        data.sheet_names()
        # 获取第一张表数据
        tables = data.sheets()[n]
        return tables

