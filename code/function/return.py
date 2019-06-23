# 问题？
	# 函数如何能返回一些数据给调用者？
	# 答案就是：return 语句
# _______________示例1__________________

# s = 1
# def myfun(a,b):
# 	s = a + b
# 	print('和是：',s)
# 	return 10000

# v = myfun(100,200)
# print('V = ',v)	# v = 10000
# print(s)		# s = 1

# _______________示例2__________________

# 创建mymax,实现两个数的最大值：
# def mymax(a,b):
# 	return b if a < b else a

# print(mymax(100,200))
# print(mymax(50,10))
# print(mymax('ABC','ABCD'))

# _______________示例3__________________

# 写一个函数 input_number
# def input_number():
# 	L = []
# 	while True:
# 		i = int(input('输入一个整数：'))
# 		if i < 0:
# 			return L
# 		L.append(i)

# L = input_number()
# print(L)
# print('用户输入的最大值是：',max(L))
# print('用户输入的最小值是：',min(L))
# print('用户输入的和是：',sum(L))