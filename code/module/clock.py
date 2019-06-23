# 练习1：
# 电子表

import time as t

def clock():
	while True:
		cur_time = t.localtime()
		time_hms = cur_time[3:6]		 
		t.sleep(1)
		print('%02d:%02d:%02d' % time_hms,end='\r')		# \r 返回光标至行首，可实现覆盖打印记录


clock()