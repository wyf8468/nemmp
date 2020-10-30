# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14
# @Author  : wangyufeng
# @Remark: 上传本地文件非input标签
import time
import unittest
"""
import win32gui
import win32con

def upload(filePath):
    # 使用win32gui和win32con对弹出的文件窗口进行控制：输入要上传的文件路径，点击打开
    # 获取文件弹窗对象【第一个对象句柄，后面的父】
    # 获取窗口位置
    # 从顶层窗口向下搜索主窗口，无法搜索子窗口
    # FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
    dialog = win32gui.FindWindow('#32770', '打开')
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, filePath)
    # 获取 打开button按钮对象
    button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)')
    # 点击 打开
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    time.sleep(3)
-------------------------------------------------------------------------
import os
import subprocess
import uiautomation
import time
def upload(filePath):
    wc = uiautomation.WindowControl(searchDepth=1, class_name='#32770')
    print(wc.ButtonControl(class_name='#32770'))
    # 设置为顶层
    wc.SetTopmost(True)
    edit = uiautomation.EditControl(class_name='Edit')
    edit.Click()
    edit.SendKeys(filePath)
    # edit.TextControl(filePath)
    time.sleep(1)
    wc.ButtonControl(class_name='Button').Click()
    time.sleep(3)
"""

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








