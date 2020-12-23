# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17
# @Author  : wangyufeng
# @Remark: 视频短信-制作视频短信
import unittest
import logging
import ddt
from nmmp_manage.common.comm_setUpClass import commSetUpClass
from nmmp_manage.pages.logic.send_videoMsg.makeVideoMsg_page import *
from nmmp_manage.pages.datas.sendVideoMsg_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    # @unittest.skip('制作视频短信模板用例无条件跳过')
    @classmethod
    def setUpClass(self):
        csuc = commSetUpClass()
        self.driver = csuc.comm_setUpClass()

    # 刷新一下当前页面
    def tearDown(self):
        self.driver.refresh()

    # 正常用例
    # @unittest.skip('制作视频短信模板用例无条件跳过')
    def test_makeVideo_1_success(self):
        logging.info("*********制作视频短信用例：点击关闭*********")
        makeVedioMsgPage(self.driver).func_basic(makeVideo_datas['name'], 0, makeVideo_datas['content'], makeVideo_datas['vedioPath'], '关闭')
        time.sleep(2)

    @unittest.skip('制作视频短信模板用例无条件跳过')
    def test_makeVideo_2_success(self):
        logging.info("*********制作视频短信用例：先文本在视频*********")
        makeVedioMsgPage(self.driver).func_basic(makeVideo_datas['name'], 0, makeVideo_datas['content'], makeVideo_datas['vedioPath'], '确认')
        time.sleep(2)

    @unittest.skip('制作视频短信模板用例无条件跳过')
    def test_makeVideo_3_success(self):
        logging.info("*********制作视频短信用例：先视频在文本*********")
        makeVedioMsgPage(self.driver).func_basic(makeVideo_datas['name'], 1, makeVideo_datas['content'], makeVideo_datas['vedioPath'], '确认')
        time.sleep(2)

    @unittest.skip('制作视频短信模板用例无条件跳过')
    def test_makeVideo_4_success(self):
        logging.info("*********制作视频短信用例：先图片在文本*********")
        makeVedioMsgPage(self.driver).func_basic(makeVideo_datas['name'], 2, makeVideo_datas['content'], makeVideo_datas['imgPath'], '确认')
        time.sleep(2)

    @unittest.skip('制作视频短信模板用例无条件跳过')
    def test_makeVideo_5_success(self):
        logging.info("*********制作视频短信用例：先文本在图片*********")
        makeVedioMsgPage(self.driver).func_basic(makeVideo_datas['name'], 3, makeVideo_datas['content'], makeVideo_datas['imgPath'], '确认')
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)
