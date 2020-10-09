import time

from nmmp_manage.common.menuUtils import *
import ddt
from nmmp_manage.common.comm_login import *
from nmmp_manage.pages.datas.login_datas import *
from nmmp_manage.common.getLists import *
from nmmp_manage.common.connectMysql import *

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
        MenuUtils(self.driver).menu_tab('li', '已发短信')
        time.sleep(2)
        comm_frame(self.driver).Frame('mainFrame_30')  # 获取iframe
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        table_tr_list = self.driver.find_element(By.ID, 'table_content').find_elements(By.TAG_NAME, "tr")
        table_list = []  # 存放table数据
        for tr in table_tr_list:  # 遍历每一个tr
            # 将每一个tr的数据根据td查询出来，返回结果为list对象
            table_td_list = tr.find_elements(By.TAG_NAME, "td")
            row_list = []
            # print(table_td_list)
            for td in table_td_list:  # 遍历每一个td
                row_list.append(td.text)  # 取出表格的数据，并放入行列表里
            table_list.append(row_list)
        queryContent = '提交成功'
        # 循环遍历table数据，确定查询数据的位置
        for i in range(len(table_list)):
            for j in range(len(table_list[i])):
                if queryContent == table_list[i][j]:
                    print("%r坐标为(%r,%r)" % (queryContent, i + 1, j + 1))
                    print(table_list[i][j])

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
