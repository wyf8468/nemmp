# --^_^-- coding:utf-8 --^_^--
# @Remark:登录测试数据

from nmmp_manage.common.comm_datas import web_login_url

# 正常场景
success_data = {"user": "27771000", "pwd": "12345@q", "rand": "1111", "check": web_login_url}

# 异常场景1
wrong_datas = [
    {"user": "", "pwd": "", "rand": "", "check": "请填写账号！"},
    {"user": "", "pwd": "", "rand": "1111", "check": "请填写账号！"},
    {"user": "", "pwd": "12345@q", "rand": "1111", "check": "请填写账号！"},
    {"user": "27771000", "pwd": "", "rand": "1111", "check": "请填写密码！"},
    {"user": "27771000", "pwd": "12345@q", "rand": "", "check": "请填写验证码！"},
    {"user": "admin", "pwd": "123456", "rand": "1111", "check": "用户不存在！"},
    {"user": "27771000", "pwd": "1234567", "rand": "1111", "check": "密码错误，请重新输入！"}
]