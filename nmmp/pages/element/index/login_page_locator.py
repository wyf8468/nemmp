# --^_^-- coding:utf-8 --^_^--
# @Remark:登录页面元素定位

from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    user_loc = (By.XPATH, '//input[@name="account"]')
    # 密码输入框
    pwd_loc = (By.XPATH, '//input[@name="pwd"]')
    # 验证码输入框
    rand_loc = (By.XPATH, '//input[@name="rand"]')
    # 登录按钮
    login_button_loc = (By.XPATH, '//input[@name="login"]')
    # 密码错误提示信息
    login_error_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/p[1]')
