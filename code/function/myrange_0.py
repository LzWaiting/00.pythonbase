# 正数，正步长range()函数：
def myrange(start,*,stop = None,step = 1):
	L = []
	if stop is None:
		stop = start
		start = 0
	while start < stop:
		L.append(start)
		start += step
	return L

print(myrange(3))
print(myrange(3,6))
print(myrange(1,10,3))