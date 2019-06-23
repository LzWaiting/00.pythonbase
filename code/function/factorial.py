# 编写函数求阶乘

# 方法1（常规循环）：
def myfac1(x):
	s = 1
	for n in range(1,x+1):
		s *= n
	return s

# 方法2（递归函数）：
def myfac2(x):
	if x == 1:
		return 1
	return x*myfac2(x-1)

# print(myfac2(4))

# 阶乘求和 1！+2！+3!+...+20!
# 方法1：
def sum_fac(x):
	if x == 1:
		return 1
	return myfac1(x) + sum_fac(x-1)

print(sum_fac(20))
# 方法2（高阶函数）：
print(sum(map(myfac1,range(1,21))))