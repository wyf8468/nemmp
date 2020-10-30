# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13
# @Author  : wangyufeng
# @Remark: 两个日期进行比较
import datetime


def date_compare(date1):
    # 满足返回True ，不满足返回False
    date = datetime.datetime.now()
    dataNow = datetime.datetime.strftime(date, '%Y-%m-%d %H:%M:%S')  # 获取当前时间
    return date1 >dataNow







