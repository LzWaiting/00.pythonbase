# 练习2：
# 闹钟程序：
import time as t 	
	
def alarm(h,m,s):	
	while True:
		cur_time = t.localtime()
		time_hms = cur_time[3:6]
		print('%02d:%02d:%02d' % time_hms,end='\r')
		if (h,m,s) == time_hms:
			break

def main():
	hour = int(input('请输入时'))
	minute = int(input('请输入分'))
	second = int(input('请输入秒'))
	alarm(hour,minute,second)
	print('您该起床了！！！')

main()