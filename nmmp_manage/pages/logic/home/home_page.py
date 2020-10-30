from nmmp_utils.selenium.SeleniumUtils import seleniumUtils
from nmmp_manage.pages.element.home.home_locator import HomePageLocator as home
import logging


class HomePage(seleniumUtils):
    # 检查登录后，首页中的元素
    def check_login_ele_exists(self):
        check_element = home.home_check
        temp = False
        try:
            # 从home_page_locator中调用某个元素判断是否存在
            if seleniumUtils.wait_eleVisible(check_element):
                temp = True
        except Exception as e:
            logging.info("主页检查元素不存在！".format(check_element))
        finally:
            return temp
