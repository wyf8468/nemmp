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

    def connect_mysql(self, database, statement, value, num):
        # 连接数据库
        conn = pymysql.connect(host='192.168.0.152', user='root', password='123456yxt', db=database)
        # 创建游标，并将其设为字段类型
        cursor = conn.cursor()
        effect_row = cursor.execute(statement)
        result = cursor.fetchall()
        # 打印所有数据
        # print(result);
        # 输出第一条数据
        # print(cursor.fetchone())
        # print(effect_row)
        # 遍历输出
        Arr = []
        for i in range(len(result)):
            # print(result[i][0])
            if result[i][1] == value:
                print(True)
                # print(result[i][num1])
                # print(result[i][0])
                dataId = result[i][num]
                # print(dataId)
                Arr.append(dataId)
                # print(i)
            # else:
                # print("找不到元素")
        # 提交
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return Arr


