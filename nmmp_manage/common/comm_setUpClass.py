
from nmmp_manage.common.comm_login import *
from nmmp_manage.pages.datas.login_datas import *
from selenium import webdriver


class commSetUpClass(object):
    def __init__(self):
        self.driver = None

    def comm_setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(web_login_url)
        self.driver.implicitly_wait(5)  # 隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时
        # 先登录
        comm_login(self.driver).Loginfor(ld.success_data["user"], ld.success_data["pwd"], ld.success_data['rand'])
        return self.driver

