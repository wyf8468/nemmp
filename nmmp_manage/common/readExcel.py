#!/usr/bin/env python
# coding=utf-8
import time
import datetime

first = '12:00'
third = '14:00'
second = '2019-08-27 13:05:20'

# 提取日期时间中的日期
date_new = datetime.datetime.strptime(second, '%Y-%m-%d %H:%M:%S').date()

# 转换为字符串，去除日期时间中的日期
time_new = str(second).replace(str(date_new), ' ').strip()

# 将要比较的字符串都转换为时间格式
first_new = datetime.datetime.strptime('12:00:00', '%H:%M:%S')
third_new = datetime.datetime.strptime('14:00:00', '%H:%M:%S')
time_new = datetime.datetime.strptime(time_new, '%H:%M:%S')

# 判断是否在12点到14点的区间内
if first_new < time_new < third_new:
    print('在12点到14点的区间内')
else:
    print('不在12点到14点的区间内')