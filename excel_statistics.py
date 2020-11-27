import xlrd
from phone import Phone
# 移动号段
var_move = ['134', '135', '136', '137', '138', '139', '147', '150',
            '151', '152', '157', '158', '159', '165', '172', '178', '182',
            '183', '184', '187', '188', '198', '195', '1703', '1705', '1706', '185', '10086']
# 电信号段
var_telecom = ['133', '141', '153', '162', '168', '173', '177', '180', '181', '189', '191', '199', '1700',
               '1701', '1702', '1740', '10000']
# 联通号段
var_link = ['130', '131', '132', '145', '146', '155', '156', '166', '167', '171', '175', '176',
            '186', '1704', '1707', '1708', '1709', '10010']
# 咨询电话
var_114 = ['114']
# 社保局
var_social = ['12333']
# 101/105/106/108/12114/102/197284不知归属地
var_unaware = ['101', '105', '106', '108', '121', '102', '197']

region_move = []


filePath = r'D:\桌面\10月通话记录2.xlsx'
num = 572838
month = '10月份-2'

data = xlrd.open_workbook(filePath)
# 查看工作表
# data.sheet_names()
# 获取第一张表数据
tables = data.sheets()[0]
i = 1
# 移动
str_move = 0
#电信
str_telecom = 0
# 联通
str_link = 0
# 其他非1开头的
str_qt = 0
# 咨询
str_114 = 0
# 社保局
str_social = 0
# 101/105/106/108
str_unaware = 0
arr = []

while i < num:

    phone = tables.cell_value(i, 0)  # 获取电话
    value = str(phone)[0:3]
    value_index = str(phone)[0:1]
    call_duration = tables.cell_value(i, 2)  # 获取对应通话时间

    if value == '170':
        value = str(phone)[0:4]

    elif value == '100':
        value = str(phone)[0:5]

    elif value =='114':
        str_114 = str_114 + call_duration

    elif value =='123':
        str_social = str_social + call_duration

    elif value in var_move:
        str_move = call_duration + str_move

    elif value in var_telecom:
        str_telecom = call_duration + str_telecom

    elif value in var_link:
        str_link = call_duration + str_link

    elif value in var_unaware:
        str_unaware = call_duration + str_unaware

    else:
        if value_index == '1':
            arr.append(phone)
        str_qt = str_qt + call_duration
    i = i+1

print('——'+month+'——')
print('移动分钟：' + str(str_move))
print('电信分钟：' + str(str_telecom))
print('联通分钟：' + str(str_link))
print('其他号段（非1开头的）固话：' + str(str_qt))
print('咨询电话114：' + str(str_114))
print('社保局12333：' + str(str_social))
print('101/105/106/108/12114/102/197284：' + str(str_unaware))
sum = str_move + str_telecom + str_link + str_qt + str_114 + str_social + str_unaware
print('汇总：' + str(sum))
print(arr)

