# --^_^-- coding:utf-8 --^_^--
# @Remark:菜单测试数据

from nmmp_manage.common.comm_datas import web_login_url

# 正常场景
success_data = {"phone": '18722221111', "content": '节日快乐-zdhmn ',  "check": web_login_url}

# 异常场景1
wrong_datas = [{"phone": '', "content": '', "check": "请输入号码!"},
               {"phone": '18722221111', 'content': '', "check": "内容不能为空!"},
               {"phone": '', "content": '节日快乐', "check": "请输入号码!"},
               {"phone": '188', "content": '', "check": "请输入号码!"},

]