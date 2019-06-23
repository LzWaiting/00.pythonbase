# 联系使用列表索引/切片
# L = [3,5]
# L[1:1] = [4]
# L[0:0] =[1,2]
# L[len(L):len(L)] = [6]
# print(L)
# L[:] = L [::-1]
# del L[-1]
# print(L)

# 方法1:
# L = list()
# while True:
# 	n = int(input("请输入一些整数:"))
# 	if n == -1:
# 		break
# 	L += [n]
# print(L)	
# print(len(L))
# print(max(L))
# print(min(L))
# print(sum(L)/len(L))
