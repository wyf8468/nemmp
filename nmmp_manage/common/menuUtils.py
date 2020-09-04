
import time
from selenium import webdriver
from nmmp_manage.pages.datas.sendMsg_datas import *

class MenuUtils:
    #选择菜单
    def select_menu(self, * menu_name):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://yxtcd.f3322.net:10080/common/')
        time.sleep(1)
        driver.find_element_by_xpath(menu_name).click()
        print(driver.current_window_handle)  # 输出当前窗口句柄
        handles = driver.window_handles  # 获取当前全部窗口句柄集合
        print(handles)  # 输出句柄集合

        for handle in handles:  # 切换窗口
            if handle != driver.current_window_handle:
                print('switch to second window', handle)
                driver.close()  # 关闭第一个窗口
                driver.switch_to.window(handle)  # 切换到第二个窗口

    select_menu(success_data['nomal_msg'])