# 递归函数练习：
L = [[3,5,8],10,[[13,14],15,18],20]
# 方法1：
# 打印所有元素：
def print_list(L):
	for x in L:
		if type(x) is list:
			print_list(x)
		else:
			print(x)
# 求列表元素和：
def sum_list(L):
	s = 0
	for x in L:
		if type(x) is list:
			s += sum_list(x)
		else:
			s += x
	return s
# 主程序：
def main():
	print_list(L)
	print(sum_list(L))	
# 方法2：
# 打印所有元素：
# def print_list(lst):
# 	L = []
# 	def list_fun(ls):
# 		for l in ls:
# 			if type(l) is list:
# 				list_fun(l)
# 			else:
# 				L.append(l)
# 	list_fun(lst)
# 	print(L)
# 	return L
# 求列表元素和：
# def sum_list(lst):
# 	for l in lst:
# 		lst.remove(l)
# 		if lst == []:
# 			return l
# 		return l + sum_list(lst)
# 主程序：
# def main():
# 	l = print_list(L)
# 	print(sum_list(l))

main()
