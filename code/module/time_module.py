import time as t

year = int(input('请输入年：'))
month = int(input('请输入月：'))
day = int(input('请输入日：'))

# 获得出生时间元组：
birthday_tuple = (year,month,day,0,0,0,0,0,0)

# 获得出生时的秒数：
birthday_second = t.mktime(birthday_tuple)

# 获得当前时间的秒数：
cur_second = t.time()

# 计算出生到现在的天数：
seconds = (cur_second-birthday_second)
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
months = days / 30
years = days / 365
print(seconds,minutes,hours,days,months,years,sep='\n')

# 计算出生时的详细信息：
# 转回到时间本地元组：
time_info = t.localtime(birthday_second)
weekday = {0:'一',1:'二',2:'三',3:'四',4:'五',5:'六',6:'日'} 
print('你出生的那天是：星期',weekday[time_info[6]])