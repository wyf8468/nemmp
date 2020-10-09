
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/07
# @Author  : wangyufeng
# @Remark: 发送普通短信基本发送-立即发送成功
import time
import unittest
from nmmp_manage.pages.datas import sendMsg_datas as msgDatas
import logging
import ddt
from nmmp_manage.pages.logic.send_msg.send_generalMsg_page import SendMsgPage
from nmmp_manage.common.menuUtils import *
from nmmp_manage.common.comm_login import *
from nmmp_manage.pages.datas.login_datas import *
from nmmp_manage.common.getLists import *
from nmmp_manage.common.connectMysql import *
from nmmp_manage.common.get_property import *

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(web_login_url)
        cls.driver.implicitly_wait(5)  # 隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时
        # 先登录
        comm_login(cls.driver).Loginfor(success_data['user'], success_data['pwd'], "1111")

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    def test_sendGeneral_2_success(self):
        temp = True
        comm_frame(self.driver).Frame('mainFrame_26')  # 获取iframe
        logging.info("*********发送普通短信用例：正常场景-立即发送提交成功*********")
        SendMsgPage(self.driver).send_normal_msg(msgDatas.success_data["phone"], msgDatas.success_data["content"])
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        SendMsgPage(self.driver).send_suceedPop()  # 点击弹窗上的确认按钮
        # SendMsgPage(self.driver).send_check()
        time.sleep(2)
        # 获取列表返回值task_id
        getDataId = getList(self.driver).get_list('mainFrame_28', 0, '//*[@id="table_content"]', 'tr', 'dataid')
        time.sleep(8)
        SendMsgPage(self.driver).send_refresh()
        # 获取短信审核箱中提交过来的审核状态
        msg_trone = self.driver.find_element_by_xpath('//*[@id="table_content"]/tbody/tr[1]/td[6]/span')
        print(msg_trone.text)
        # 断言：判断结果信息是否一致
        self.assertEqual(msgDatas.success_data["checkText"], msg_trone.text)
        if msg_trone.text == msgDatas.success_data["checkText"]:
            self.driver.switch_to.default_content()  # 释放iframe
            time.sleep(1)
            MenuUtils(self.driver).menu_tab('li', '已发短信')
            time.sleep(2)
            comm_frame(self.driver).Frame('mainFrame_30')  # 获取iframe
            # 连接数据库循环判断已发短信是否有对应id
            Arr = connectMysql(self.driver).connect_mysql('nemmp_sms_zk', "SELECT * FROM `sms_task_contact_202010`", int(getDataId), 0)
            for id in Arr:
                msg_alreadyTr = self.driver.find_element_by_css_selector('[dataid="'+str(id)+'"]')  # 通过dataid属性定位元素
                # 获取属性为'sendStatus'的元素
                msg_text = getProperty(self.driver).get_pro(msg_alreadyTr, 'sendStatus')
                # 获取属性为'statusCodeCh'的元素
                msg_remark = getProperty(self.driver).get_pro(msg_alreadyTr, 'statusCodeCh')
                # 判断发送状态与预期是否相符
                if msgDatas.success_data["codeText"] != msg_text.text:
                    print(msg_alreadyTr.text)
                    print(msg_text.text)
                    print('代码注释：' + msg_remark.text)
                    temp = False
                    break
        self.assertTrue(temp)

    # 异常用例
    @unittest.skip('普通短信下发用例无条件跳过')
    @ddt.data(*msgDatas.wrong_datas)
    def test_sendGeneral_1_error(self, data):
        # 获取iframe
        comm_frame(self.driver).Frame('mainFrame_26')
        # 选择菜单到发送普通短信页面
        MenuUtils(self.driver).menu_tab('li', '发送普通短信')
        time.sleep(2)
        # 判断收件号码方式
        MenuUtils(self.driver).menu_tab('li', '手动输入')
        time.sleep(2)
        logging.info("*********发送普通短信用例：异常场景-取消立即发送提交失败*********")
        SendMsgPage(self.driver).send_normal_msg(data["phone"], data["content"])
        SendMsgPage(self.driver).send_immediately()  # 立即发送
        SendMsgPage(self.driver).send_submit()  # 提交发送
        self.driver.switch_to.default_content()  # 释放iframe
        time.sleep(2)
        # 断言：判断提示信息是否一致
        self.assertEqual(data["check"], SendMsgPage(self.driver).get_errorMsg())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
        """
        verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
        0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
        1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
        2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
        
        """



