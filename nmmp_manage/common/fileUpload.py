# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14
# @Author  : wangyufeng
# @Remark: 上传本地文件非input标签
import time
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
    # 获取窗口位置
    left, top, right, bottom = win32gui.GetWindowRect(Edit)
    # 获取某个句柄的类名和标题
    title = win32gui.GetWindowText(Edit)
    clsname = win32gui.GetClassName(Edit)
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, filePath)
    print(left, top, right, bottom)
    # 获取 打开button按钮对象
    button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)')
    # 点击 打开
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    time.sleep(3)

"""

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









