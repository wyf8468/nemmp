from nmmp_manage.common.comm_datas import *
from selenium import webdriver
class comm_frame:


    def __init__(self, driver):
        self.driver = driver
    # 定义登陆函数，将登陆作为公共调用的模块，进行数据传递,因此不需要导入webdriver这个模块
    def Frame(self,  frame):

        # 登录后的
        self.driver.switch_to_frame(self.driver.find_element_by_id(frame))  # 获取当前frame
