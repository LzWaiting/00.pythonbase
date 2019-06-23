print("生成前40斐波那契数(Fibonacci)")

# 方法1(an表达式):
# L = [1,1]
# for i in range(38):
# 	L.append(L[-1]+L[-2])

# while len(L) < 40:
# 	L.append(L[-1]+L[-2])

# 方法2(递推数列):
a = 0
b = 1	# 代表第一个数
L = []
while len(L) < 40:
	a, b = b, a + b
	L.append(a)		# 元组思想

print(L)