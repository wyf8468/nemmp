# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14
# @Author  : wangyufeng
# @Remark: 上传本地文件非input标签
import time
import unittest
import win32api
import win32con
import time
import pyperclip


def UpLoad_File(filePath):
    """
    使用 python 的 win32api，win32con 模拟按键输入，实现文件上传操作。
    :param webEle: 页面中的上传文件按钮,是已经获取到的对象
    :param filePath: 要上传的文件地址，绝对路径。如：D:\work\账号调账模板.xlsx
    """
    pyperclip.copy(filePath)  # 复制文件路径到剪切板
    time.sleep(3)  # 等待程序加载 时间 看你电脑的速度 单位(秒)
    # 发送 ctrl（17） + V（86）按钮
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)
    win32api.keybd_event(13, 0, 0, 0)  # (回车)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
    time.sleep(2)








