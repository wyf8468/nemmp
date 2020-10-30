# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28
# @Author  : wangyufeng
# @Remark: 查询数据库

import pymysql
class connectMysql:
    def __init__(self, driver):
        self.driver = driver

    def connect_mysql(self, ip, database, statement, value, num):
        # 连接数据库
        conn = pymysql.connect(host=ip, user='root', password='123456yxt', db=database)
        # 创建游标，并将其设为字段类型
        cursor = conn.cursor()
        effect_row = cursor.execute(statement)
        result = cursor.fetchall()
        # 遍历输出
        Arr = []
        for i in range(len(result)):
            if result[i][1] == value:
                dataId = result[i][num]
                Arr.append(dataId)
        # 提交
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return Arr


