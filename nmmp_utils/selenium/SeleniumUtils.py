# --^_^-- coding:utf-8 --^_^--
# @Remark:webdriver的封装

from nmmp_utils.log import logUtil
import logging
import time
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nmmp_manage.common.dir_config import screenshot_dir
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class seleniumUtils:
    '''
    包含了PageObjects当中，用到所有的selenium底层方法。
    还可以包含通用的一些元素操作，如alert,iframe,windows...
    还可以自己额外封装一些web相关的断言
    实现日志记录、实现失败截图
    '''
    def __init__(self, driver):
        self.driver = driver

    # 实现网页截图操作
    def save_web_screenshot(self, img_doc):
        # 页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}-{}.png".format(now, img_doc)
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logging.info("网页截图成功！图片存储在：{}!".format(screenshot_dir + "/" + filepath))
        except:
            logging.exception("网页截图失败！")
            raise

    # 等待元素可见
    def wait_eleVisible(self, loc, img_doc="", timeout=30, frequency=0.5):
        logging.info("等待元素{}可见！".format(loc))
        try:
            # 起始等待的时间datetime
            startTime = datetime.datetime.now()
            # 等待元素
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located)
            # 结束等待时间
            endTime = datetime.datetime.now()
            logging.info("等待元素成功！开始等待时间：{}，结束等待时间：{}，等待时长为：{}！".format(startTime,
                                                                       endTime,
                                                                       endTime - startTime))
        except:
            # 日志
            logging.exception("等待元素可见失败！")
            # 截图-哪一个页面哪一个操作导致的失败 + 当前时间
            self.save_web_screenshot(img_doc)
            raise

    # 查找一个元素
    def get_element(self, loc, img_doc=""):
        '''
        :param loc: 元素定位，以元组的形式。（定位类型、定位时间）
        :param img_doc:截图的说明。例如：登录页面_输入用户名
        :return:webElement对象。
        '''
        logging.info("查找{}中的元素{}".format(img_doc, loc))
        try:
            ele = self.driver.find_element(*loc)
            logging.info("查找{}元素成功！".format(ele))
            return ele
        except:
            # 日志
            logging.exception("查找元素失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 等待元素出现，点击元素
    def click_element(self, loc, img_doc, timeout=30, frequency=0.5):
        '''
        :param loc:元素定位，以元组的形式。（定位类型、定位时间）
        :param img_doc:截图的说明。例如：登录页面_输入用户名
        :param timeout:等待元素的超时上限
        :param frequency:等待元素可见时，轮询周期
        :return:
        '''
        # 等待元素可见
        self.wait_eleVisible(loc, img_doc, timeout, frequency)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 点击操作
        logging.info("点击元素{}！".format(loc))
        try:
            ele.click()
            logging.info("点击元素{}成功！".format(ele))
        except:
            # 日志
            logging.exception("点击元素失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 文本输入
    def input_text(self, loc, img_doc, *args):
        '''
        等待元素可见，找到元素，并在元素中输入文本信息
        :param loc:元组形式的元素定位表达式
        :param img_doc:执行失败时，截图的文件命名
        :param args:输入操作中，可以输入多个值，也可以组合按键
        :return:
        '''
        # 等待元素出现
        self.wait_eleVisible(loc, img_doc)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 清空输入框内容
        self.clear_data(loc, img_doc)
        # 文本输入
        logging.info("给元素{}输入文本内容：{}".format(loc, *args))
        try:
            ele.send_keys(*args)
            logging.info("文本输入成功！")
        except:
            # 日志
            logging.exception("文本输入失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_doc):
        '''
        获取元素标签的内容
        :param loc:元素定位，以元组的形式。（定位类型、定位时间）
        :param attr_name:属性名称
        :param img_doc:执行失败时，截图的文件命名
        :return:
        '''
        # 等待元素出现
        self.wait_eleVisible(loc, img_doc)
        # 查找元素
        ele = self.get_element(loc, img_doc)
        # 获取属性
        try:
            attr_value = ele.get_attribute(attr_name)
            logging.info("获取元素{}的属性{}值为：{}！".format(loc, attr_name, attr_value))
            return attr_value
        except:
            # 日志
            logging.exception("获取元素属性失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的文本值
    def get_element_text(self, loc, img_doc):
        '''
        :param loc:元素定位，以元组的形式。（定位类型、定位时间）
        :param img_doc:执行失败时，截图的文件命名
        :return:
        '''
        # 等待元素出现
        self.wait_eleVisible(loc, img_doc)
        # 查找元素
        ele = self.get_element(loc,img_doc)
        # 获取文本值
        try:
            text = ele.text
            logging.info("获取元素{}的文本值为：{}！".format(loc, text))
            return text
        except:
            # 日志
            logging.exception("获取元素文本值失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 鼠标悬浮操作
    def mouse_suspension(self,loc, img_doc):
        # 实例化ActionChains
        ac = ActionChains(self.driver)
        # 等待元素出现
        self.wait_eleVisible(loc, img_doc)
        # 查找元素
        ele = self.get_element(loc)
        # 鼠标悬浮
        try:
            ac.move_to_element(ele).perform()
            time.sleep(1)
            logging.info("鼠标悬浮成功！")
        except:
            # 日志
            logging.exception("鼠标悬浮失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 进入到iframe中
    def get_iframe(self,loc,img_doc):
        # 等待元素出现
        self.wait_eleVisible(loc, img_doc)
        # 查找元素
        ele = self.get_element(loc)
        # 进入iframe
        try:
            self.driver.switch_to.frame(ele)
            logging.info("进入iframe中成功！")
        except:
            # 日志
            logging.exception("进入到iframe中失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 通过文本选择下拉选择框
    def drop_down_select(self,loc,text,img_doc):
        # 等待元素出现
        self.wait_eleVisible(loc, img_doc)
        # 查找select元素
        ele = self.get_element(loc)
        # 下拉选择
        try:
            Select(ele.select_by_visible_text(text))
            logging.info("选择select成功！")
        except:
            # 日志
            logging.exception("下拉选择失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 选择非select的下拉选择框
    def drop_down_not_select(self, loc1, loc2, img_doc):
        # 先定位到下拉菜单
        # 等待元素出现
        self.wait_eleVisible(loc1, img_doc)
        # 查找下拉菜单元素
        self.click_element(loc1, "下拉菜单输入框")
        logging.info("查找下拉菜单输入框成功！")
        time.sleep(2)
        # 在对下拉菜单的选项进行选择
        try:
            # 选择下拉菜单选项
            # 等待元素出现
            self.wait_eleVisible(loc2, img_doc)
            self.click_element(loc2,"选择下拉菜单选项")
            logging.info("选择下拉菜单成功！")
        except:
            # 日志
            logging.exception("下拉选择失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 清空输入框中的内容
    def clear_data(self, loc, img_doc):
        # 等待元素出现
        self.wait_eleVisible(loc, img_doc)
        # 查找一个元素
        ele = self.get_element(loc)
        # 清空输入框
        try:
            ele.clear()
            logging.info("清空输入框成功！")
        except:
            # 日志
            logging.exception("清空输入框失败！")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 上传操作（前提 ：windows上传窗口已经出现。sleep1-2秒等待弹出的出现。）
    def upload(filePath, browser_type="chrome"):
        if browser_type == "chrome":
            title = "打开"
        else:
            title = ""


        # # 找元素
        # # 一级窗口"#32770","打开"
        # dialog = win32gui.FindWindow("#32770", title)
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        # comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # # 编辑按钮
        # edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # # 打开按钮
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 四级
        #
        # # 往编辑当中，输入文件路径.
        # win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮