# --^_^-- coding:utf-8 --^_^--
# @Remark:登录页面

from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.index.login_locator import LoginPageLocator as login


class LoginPage(seleniumUtils):

    # 登录功能
    def login(self, username, pwd, rand):
        self.input_text(login.user_loc, "登录页面_输入用户名", username)
        self.input_text(login.pwd_loc, "登录页面_输入密码", pwd)
        self.input_text(login.rand_loc, "登录页面_输入验证码", rand)
        self.click_element(login.login_button_loc, "登录页面_点击登录按钮")

    # 获取登录失败提示信息
    def get_errorMsg(self):
        return self.get_element_text(login.login_error_loc, "登录失败错误提示！")
