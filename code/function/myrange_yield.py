'''仿制range函数功能,写一个生成器函数myrange,可实现1,2,3个参数传参,生成正向整数
'''
def myrange(start = 0,stop = None,step = 1):
	if not stop:
		stop = start
		start = 0 
	_ = start
	while _ < stop:
		yield _ 
		_ += step

if __name__ == '__main__':
	for x in myrange(1,10,3):
		print(x)	
