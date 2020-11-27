# coding:utf8
import xlrd
from phone import Phone

p = Phone()
c = '15854648273'  # 手机号
city = p.find(c)
print(city)  # 所有信息
print('手机号：' + c)
print('所属省份：' + city['province'])
print('所属市区：' + city['city'])
print('邮    编：' + city['zip_code'])
print('电话区号：' + city['area_code'])
print('运 营 商：' + city['phone_type'])