

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

    def menu_tab(self, label, value):
        for meuLab in self.driver.find_elements_by_tag_name(label):
            # print(meuLab.text)
            if (meuLab.text == value):
                # print(True)
                meuLab.click()
                break







