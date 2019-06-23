# 用 def 语句来创建函数 及 自定义函数的调用 
def mymax(a,b):
	print('a = ',a)
	print('b = ',b)
	if a > b:
		print(a,"大于",b)
	else:
		print(a,"不大于",b)

# 调用mymax() 函数
x = 27
y = 18
mymax(x,y)