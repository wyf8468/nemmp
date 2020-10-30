# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28
# @Author  : wangyufeng
# @Remark: 获取列表数据
from nmmp_manage.common.comm_frame import *


class getList(object):
    def __init__(self, driver):
        self.driver = driver

    def get_list(self, frame, n, table, label, nature):
        comm_frame(self.driver).Frame(frame)  # 获取iframe
        menu_table = self.driver.find_element_by_xpath(table)
        list = menu_table.find_elements_by_tag_name(label)
        # before_add_numbers = len(list)
        # print(before_add_numbers)
        getDataId = list[int(n)].get_attribute(nature)
        # print(getDataId)
        return getDataId




