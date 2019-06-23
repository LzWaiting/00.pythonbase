# 练习3：
# 求多项式的和(e的计算程序)：

import math as m

def fun(n):
	sn = sum(map(lambda x: 1/m.factorial(x),range(n+1)))
	print('当n =',n,'时，fun(',n,')=',sn)
	print('e =',m.e)
	return sn

def main():
	n = int(input('请输入一个整数：'))
	fun(n)

main()