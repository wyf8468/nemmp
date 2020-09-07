from nmmp_manage.common.comm_datas import *
from selenium import webdriver
class comm_login:


    def __init__(self, driver):
        self.driver = driver
    # 定义登陆函数，将登陆作为公共调用的模块，进行数据传递,因此不需要导入webdriver这个模块
    def Loginfor(self, username, password, code, frame):
        # 输入用户名和密码,点击登录
        user_log = self.driver.find_element_by_id("username")
        user_log.clear()
        user_log.send_keys(username)
        password_log = self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/input[2]')
        password_log.clear()
        password_log.send_keys(password)
        code_log = self.driver.find_element_by_xpath('//*[@id="validateCode"]')
        code_log.clear()
        code_log.send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        # 登录后的
        #self.driver.switch_to_frame(self.driver.find_element_by_id(frame))  # 获取当前frame
        self.driver.switch_to.frame(frame)