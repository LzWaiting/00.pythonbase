# 练习3---打印水仙花数(Narcissistic number)
# abc = a ** 3 + b ** 3 + c ** 3 
# sum = 0

# 方法1(地板除):
# for n in range(100,1000):
# 	if n == ((n // 100) ** 3 + (n % 100 // 10) ** 3 + (n % 10) ** 3):
# 		print(n,end = " ")
# 		sum += n
# print()

# 方法2(字符串切片):
# for n in range(100,1000):
# 	b = int(str(n)[0])
# 	s = int(str(n)[1])
# 	g = int(str(n)[2])
# 	if n == b ** 3 + s ** 3 + g ** 3:
# 		print(n,end = " ")
# 		sum += n
# print(sum)

# 方法3(多层循环嵌套,钟表原理):
# for b in range(1,10):
# 	for s in range(10):
# 		for g in range(10):
# 			x = 100*b + 10*s + g
# 			if x == b**3 + s**3 + g**3:
# 				print(x)
