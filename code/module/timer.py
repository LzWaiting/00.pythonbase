
order_on = input('是否要开始记时，确认请输入on:')

# def timer():
import time
s = 0
m = 0
h = 0
while order_on == 'on':
	t = (h,m,s)
	time.sleep(0.01)
	s += 1
	if s == 100:
		m += 1
		s = 0
		if m == 60:
			h += 1
			m = 0
			if h == 60:
				h = 0 
	print('%02d:%02d:%02d' % t,end='\r')

	