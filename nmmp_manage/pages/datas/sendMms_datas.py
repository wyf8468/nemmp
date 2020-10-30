# 制作彩信
import random

makeMms_data = {"phone": '187'+''.join(random.sample("1234567890", 8)), "title": '节日快乐', "content": '中秋节快乐呀！',
                'imgs': r'D:\files\images\u=2655716706,3663934570&fm=26&gp=0.jpg', 'time': '2020-10-13 10:50:55'}

# 发送个性彩信
success_pMmsDatas = {"phone": r'D:\files\模板\2003excel.xls', "title": '节日快乐', "content": '中秋节快乐呀！', 'imgs': r'D:\files\images\u=2655716706,3663934570&fm=26&gp=0.jpg'}