# --^_^-- coding:utf-8 --^_^--
# @Remark:首页页面元素定位

from selenium.webdriver.common.by import By
from nmmp.common.SeleniumUtils import seleniumUtils


class HomePageLocator:

    # 主页检查点1元素
    home_check = (By.XPATH, '//input[@id="xxxx"]')
