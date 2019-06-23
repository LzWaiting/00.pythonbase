# for x in range(5):
# 	if x == 2:
# 		continue
# 	print(x)

# 打印 begin~end 所有的偶数:
# begin = int(input("请输入一个整数:"))
# end = int(input("请输入一个大于上面的整数:"))
# for x in range(begin,end+1):
# 	if x % 2 == 1:
# 		continue
# 	print(x,end = " ")
# print()

# for x in range(begin,end+1):
# 	if x % 2 == 0:
# 		print(x,end= " ")
# 	else:
# 		pass
# print()

# while 语句使用continue时,注意死循环:
# i = 0
# while i <= 10:
# 	if i % 2 == 1:
# 		i += 1		# 避免死循环
# 		continue
# 	print(i,end = " ")
# 	i += 1
# print()