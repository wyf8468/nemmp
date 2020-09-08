# --^_^-- coding:utf-8 --^_^--
# @Remark:菜单测试数据

from nmmp_manage.common.comm_datas import web_login_url

# 正常场景文本输入
success_data = {"phone": '18788886666', "content": '节日快乐-zdh'}

# 异常场景1文本输入
wrong_datas = [
    {"phone": '', "content": '', "check": "请输入号码！"},
    {"phone": '18722221111', 'content': '', "check": "内容不能为空！"},
    {"phone": '', "content": '节日快乐', "check": "请输入号码！"},
    {"phone": '', "content": '节日快乐', "check": "请输入号码！"},
    {"phone": '188', "content": '', "check": "请输入号码！"}

]

# 正常场景-定时时间
success_timeingData = {"phone": '18788886666', "content": '生日快乐-zdh', "time": '2020-09-08 15:10:00'}

# 异常场景-定时时间
wrong_timeingData = {"phone": '18766667777', "content": '生日快乐呀-zdh', "time": '', 'check': '请输入定时时间！'}

# 清除收件号码
success_clearPhone = {"phone": "18864562345;15522221111;18731112222;17734243211;19943432123;0952345678;13945677654;17311112222;987654321;6656789", "content": '你好'}

# 双回*退订
success_unreg = [
    {"phone": '18722221111', "content": '节日快乐', "check": ""},
    {"phone": '18722221111', 'content': '节日快乐回t退', "check": "短信内容中含有双回T退，请修改！"},
    {"phone": '18722221111', "content": '节日快乐回T退', "check": "短信内容中含有双回T退，请修改！"},
    {"phone": '18722221111', "content": '节日快乐回T退订', "check": "短信内容中含有双回T退订，请修改！"},
    {"phone": '18722221111', "content": '节日快乐TD退订', "check": "短信内容中含有双TD退订，请修改！"},
    {"phone": '18722221111', "content": '节日快乐回N退订', "check": "短信内容中含有双回N退订，请修改！"},
    {"phone": '18722221111', "content": '节日快乐td退订', "check": "短信内容中含有双TD退订，请修改！"},
    {"phone": '18722221111', "content": '节日快乐退订回t', "check": "短信内容中含有双退订回T，请修改！"},
    {"phone": '18722221111', "content": '节日快乐退订回D', "check": "短信内容中含有双退订回D，请修改！"}
]
