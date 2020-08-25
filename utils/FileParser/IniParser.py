#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author：wangyufeng
# @Date  : 2020/8/24
# @Desc  :python读取ini配置的类封装

import configparser
import os

class IniCfg():
    # 定义初始化的方法
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.cfgpath = ''

    def checkSection(self, section):
        try:
            self.conf.items(section)
        except Exception:
            print('>> 无此section,请核对[%s]' % section)
            return None
        return True

    # 读取ini,并获取所有的section名
    def readSectionItems(self, cfgpath):
        if not os.path.isfile(cfgpath):
            print('>> 无此文件，请核对路劲[%s]' % cfgpath)
            return None
        self.cfgpath = cfgpath
        self.conf.read(cfgpath, encoding="utf-8")
        return self.conf.sections()

    # 读取一个section， List里面对象是元组
    def readOneSection(self, section):
        try:
            item = self.conf.items(section)
        except Exception:
            print(">> 无此section，请核对[%s]" % section)
            return None
        return item

    # 读取一个section到字典中
    def prettySecToDic(self, section):
        if not self.checkSection(section):
            return None
        res = {}
        for key, val in self.conf.items(section):
            res[key] = val
        return res

    # 读取所有section到字典中
    def prettyAllSecToDic(self):
        res_1 = {}
        res_2 = {}
        sections = self.conf.sections()
        for sec in sections:
            for key, val in self.conf.items(sec):
                res_2[key] = val
            res_1[sec] = res_2.copy()
            res_2.clear()
        return res_1

    # 删除一个section中的一个item（以键值KEY为标识）
    def removeOneItem(self, section, key):
        if not self.checkSection(section):
            return
        self.conf.remove_option(section, key)

    # 删除整个section这一项
    def removeSection(self, section):
        if not self.checkSection(section):
            return
        self.conf.remove_section(section)

    # 添加一个section
    def addSection(self, section):
        self.conf.add_section(section)

    # 往section中添加key和value
    def addItem(self, section, key, value):
        if not self.checkSection(section):
            return
        self.conf.set(section, key, value)

    # 执行write写入， remove和set方法并没有真正的修改ini文件内容，只有当执行conf.write()方法的时候，才会修改ini文件内容
    def actionOperation(self, mode):
        if mode == 'r+':
            self.conf.write(open(self.cfgpath, "r+", encoding="utf-8"))
        elif mode == 'w':
            self.conf.write(open(self.cfgpath, "w"))
        elif mode == 'a':
            self.conf.write(open(self.cfgpath, "a"))

cfgpath = r'C:\Users\cdlx\PycharmProjects\nemmp\config\config.ini'

inicfg = IniCfg()
sections = inicfg.readSectionItems(cfgpath)
print(sections)
content = inicfg.readOneSection('chaoji')
print(content)
dic = inicfg.prettySecToDic('chaoji')
print(dic)
dic = inicfg.prettyAllSecToDic()
print(dic)
inicfg.addSection('chaoji22')

content = inicfg.readOneSection('chaoji')
print(content)