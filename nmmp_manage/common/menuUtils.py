
import time
from selenium import webdriver
from nmmp_manage.pages.datas.login_datas import success_data
from nmmp_manage.pages.element.index.login_page_locator import *
from nmmp_manage.pages.element.index.login_page_locator import *
from nmmp_manage.common.comm_datas import *
from nmmp_manage.pages.datas.login_datas import *


class MenuUtils:
    #选择菜单
    """
    url = web_login_url
    driver = webdriver.Chrome()
    driver.get(url)
    locator = LoginPageLocator  # 元素定位
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(success_data['user'])
    driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/input[2]').send_keys(success_data['pwd'])
    driver.find_element_by_xpath('//*[@id="validateCode"]').send_keys('1111')
    driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
    """
    def __init__(self, driver):
        self.driver = driver
    def menu_tab(self,value):

        for li in self.driver.find_elements_by_tag_name("li"):
            print(li.text)
            if (li.text == value):
                print(True)
                li.click()






