# 发送普通邮件
import random

gemail_datas = {'address': '1659246239@qq.com', 'name': '优讯通', 'title': '节日快乐', 'time': '2020-10-28 15:00:00'}

# 发送个性邮件
success_pemailDatas = {'address': r'D:\files\模板\gx2007excel.xlsx', 'name': '优讯通', 'title': '节日快乐'}

# 制作邮件模板
makeVideo_datas = {'title': '你好—'+''.join(random.sample("qwertyuiopasdfghjkl", 3)), 'content': '祝您身体健康！'}