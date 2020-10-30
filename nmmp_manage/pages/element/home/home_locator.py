# --^_^-- coding:utf-8 --^_^--
# @Remark:首页页面元素定位

from selenium.webdriver.common.by import By
from nmmp_utils.selenium.SeleniumUtils import seleniumUtils


class HomePageLocator:

    def __init__(self):
        pass

    # 主页检查点1元素
    home_check = (By.XPATH, '//input[@id="xxxx"]')
