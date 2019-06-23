# n = int(input("请输入一个整数:"))
# if n < 2:
# 	print("不是素数")
# 	exit()
# (传统做法):
# flag = True
# for s in range(2,n):
# 	if n % s == 0:
# 		flag = False
# 		break
# if flag == True:
# 	print("素数")
# else:
# 	print("不是素数")

# 方法2:
# for s in range(2,n):
# 	if n % s == 0:
# 		print("不是素数")
# 		break
# else:
# 	print("素数") 
