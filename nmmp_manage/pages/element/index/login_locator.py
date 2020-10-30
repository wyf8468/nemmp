# --^_^-- coding:utf-8 --^_^--
# @Remark:登录页面元素定位

from selenium.webdriver.common.by import By


class LoginPageLocator:

    def __init__(self):
        pass

    # 用户名输入框
    user_loc = (By.XPATH, '//*[@id="username"]')
    # 密码输入框
    pwd_loc = (By.XPATH, '//*[@id="form"]/div/div[2]/input[2]')
    # 验证码输入框
    rand_loc = (By.XPATH, '//*[@id="validateCode"]')
    # 登录按钮
    login_button_loc = (By.XPATH, '//*[@id="loginBtn"]')
    # 密码错误提示信息
    login_error_loc = (By.XPATH, '//*[@id="form"]/div/div[1]/div')
