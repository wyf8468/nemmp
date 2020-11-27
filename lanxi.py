"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://yxt1219.f3322.net:30080/#/admin')

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div/input').send_keys('1001')
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/input').send_keys('qazwsx123')
tab = ActionChains(driver)
# 获取滑动按钮
dragElement = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# 使用随机数确定滑动位置后滑动
time.sleep(2)
# tab.drag_and_drop_by_offset(hua1, int(268), 0).perform()
driver
# 滑动结束后释放鼠标
# tab.move_to_element(hua1).release()
"""
import xlrd
from phone import Phone

pathIn = r'D:\桌面\8月外呼记录.xlsx'
pathOut = r"D:\桌面\results.txt"
num = 95668
p = Phone()
phones = []
name = '其他'
count_qt = 0
arr = {name: count_qt}
count = 0
n = 0
i = 1
data = xlrd.open_workbook(pathIn)
tables = data.sheets()[0]
arr_two = []
while i < num:
    phone = int(tables.cell_value(i, 0))  # 获取电话
    call_duration = tables.cell_value(i, 2)  # 获取对应通话时间
    call_duration = "%.3f" % call_duration

    # print(call_duration)
    phones.append(phone)
    # print(phones)
    if len(str(phone)) == 11:
        province = p.find(phone)['province']
        city = p.find(phone)['city']
        location = province + city
        arr[location] = count
        if location in arr.keys():
            count = float(call_duration) + float(count)
            arr[location] = count
            print(arr)
    else:
        arr_two.append(phone)
        print(arr_two)




    """
    
    """
    i = i+1
    #print(i)

# print(arr)
