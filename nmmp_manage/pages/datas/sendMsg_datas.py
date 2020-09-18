# --^_^-- coding:utf-8 --^_^--
# @Remark:菜单测试数据


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

# 双回*退订-正常场景
success_unreg = {"phone": '18722221111', "content": '节日快乐-zdh回t退', "check": "短信内容中含有双回T退，请修改！"}

# 双回*退订-异常场景
wrong_unreg = [
    {'content': '节日快乐-zdh回t退', "check": "短信内容中含有双回T退，请修改！"},
    {"content": '节日快乐-zdh回T退', "check": "短信内容中含有双回T退，请修改！"},
    {"content": '节日快乐-zdh回T退订', "check": "短信内容中含有双回T退订，请修改！"},
    {"content": '节日快乐-zdhTD退订', "check": "短信内容中含有双TD退订，请修改！"},
    {"content": '节日快乐-zdh回N退订', "check": "短信内容中含有双回N退订，请修改！"},
    {"content": '节日快乐-zdhtd退订', "check": "短信内容中含有双TD退订，请修改！"},
    {"content": '节日快乐-zdh退订回t', "check": "短信内容中含有双退订回T，请修改！"},
    {"content": '节日快乐-zdh退订回D', "check": "短信内容中含有双退订回D，请修改！"}
]

# 链接跟踪-正常场景
success_linkData = {"phone": '15588889999', "content": '节日快乐www.baidu.com-zdh回t退', 'check1': '开启后因链接有调整，短信计费条数可能会变化，和原有计费条数不一致。短信计费按照实际下发字符数量计费，请认真核查计费条数，'+
    '该功能免费使用！', "check2": " 1. 建议号码和链接前后添加空格，以方便客户直接点击和拨打电话！'2.短信内容中含有双回T退，请修改！"}

# 链接跟踪-异常场景
wrong_linkData = [
    {"phone": '15588889999', "content": '节日快乐www.com-zdh回t退', "check1": "短信内容未检测到可替换链接，请重新检查！一旦开启链接点击跟踪后，原链接替换为可跟踪链接，不影响用户访问网页，但每条短信计费条数会有变化，请谨慎操作！"},
    {"phone": '15588889999', "content": 'www.baidu.com-zdh回t退', 'check1': '开启后因链接有调整，短信计费条数可能会变化，和原有计费条数不一致。短信计费按照实际下发字符数量计费，请认真核查计费条数，'+
    '该功能免费使用！', "check2": " 1. 建议号码和链接前后添加空格，以方便客户直接点击和拨打电话！'2.短信内容中含有双回T退，请修改！"},
    {"phone": '15588889999', "content": 'www.baidu.nihao.com-zdh', 'check1': '开启后因链接有调整，短信计费条数可能会变化，和原有计费条数不一致。短信计费按照实际下发字符数量计费，请认真核查计费条数，'+
    '该功能免费使用！', "check2": " 1. 建议号码和链接前后添加空格，以方便客户直接点击和拨打电话！'2.短信内容中含有双回T退，请修改！"}

]
# 短信计费
billing_datas = [
    {"content": '发的格式等各环节的更好的结果价格的时间过得好发给世界观的风格的gffg工商登记vgdjfgdsjfg1大姐夫是大法官dgdf对方身份的蝶的-zdh', 'check': '2'},
    {"content": '发的格式等各环节的更好的结果价格-zdh', 'check': '1'},
    {"content": '发的格式等各环节的更好的结果价格水电费的时间过得好发给世界观的风格的工商登记vgdjfgdsjfg鬼地方个地方1大姐夫是大法官dgdf对方身份的水电费水电费沙发沙发斯蒂芬fasfasfsafsdfsfsfsdfsdfsdfsdfsdfdsfsdfsdsdfsdfdsf蝶的-zdh', 'check': '3'}

]

# 提取号码总数
extract_phoneNum = [
    {"phone": "", "check": "0"},
    {"phone": "18722221111", "check": "1"},
    {"phone": "18722221111;15588887777", "check": "2"},
    {"phone": "18722221111;15588887777,1662222", "check": "3"},
    {"phone": "18722221111;15588887777,15588887777", "check": "3"},
]
# 提取号码错误号码
extract_errorPhone = [
    {"phone": "", "check": "0"},
    {"phone": "18722221111;15588887777;1662222", "check": "1"},
]
# 提取号码重复号码
extract_repetitionPhone = [
    {"phone": "", "check": "0"},
    {"phone": "18722221111;15588887777;15588887777", "check": "1"},
]
# 提取号码有效号码
extract_validPhone = [
    {"phone": "", "check": "有效号码：0"},
    {"phone": "18722221111;15588887777;15588887777", "check": "有效号码：2"},
    {"phone": "18722221111;15588887777;1662222", "check": "有效号码：2"},
]

# 发送个性短信
personality_success = {'filePath': r"D:\files\模板\个性短信模板.xlsx", 'text': '个性短信呀'}

# 发送生日短信
birthday_success = {'filePath': r"D:\files\模板\生日短信模板 (1).xlsx", 'content': '生日快乐呀', 'days': '生日当天', 'hour': '8时', 'imune': '00分'}