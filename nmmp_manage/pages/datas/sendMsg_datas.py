# --^_^-- coding:utf-8 --^_^--
# @Remark:菜单测试数据

from nmmp_manage.common.comm_datas import web_login_url

# 正常场景
success_data = {"phone": '18722221111', "content": '节日快乐', "nomal_msg": '', "check": 'http://yxt1219.f3322.net:4042/common/frame?sid=1e41b58b18f5feccbdfa8364d34625b8'}

# 异常场景1
wrong_datas = [{"phone": '', "content": '',
                "phone": '18722221111',
                "content": '',
                "phone": '', "content": '节日快乐',
                "phone": '188', "content": '',
                "phone": '', "content": '节日快乐',
                "phone": '15523212423,34342323212', "content": '节日快乐'}
    ]