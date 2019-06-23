# 使用 input,print 进行输入输出

# 案例一：
# age = input("请输入小明的年龄")
# year = 365
# ages = int(age) 
# week = ages * year // 7
# day = ages * year % 7
# print ("小明过了",week,"个星期，余",day,"天")

# 案例二：
# s = input ("请输入当前时间小时:")
# hour = int(s)
# s = input ("请输入当前时间分钟:")
# minute = int (s)
# s = input ("请输入当前时间秒数:")
# second = int (s)
# seconds = hour * 60**2 + minute * 60 + second
# print ("现在距离凌晨已经过去",seconds,"秒")

# 案例三：
# s = input("请输入一个整数：")
# num = int(s)
# if num % 2 == 0:
# 	print ("您所输入的数",num,"是：偶数")
# else:
# 	print ("您所输入的数",num,"是：奇数")

# 案例四： 
# num = int(input("请任意输入一个数："))
# if num <= 100 :
# 	print ("您所输入的数不大于100")
# 	if num >= 0:
# 		print ("您所输入的数不小于0，且不大于100")
# 		if 20 <= num <= 50:
# 			print ("您所输入的数在20~50之间")
# 		else:
# 			print ("您所输入的数不在20~50范围内")
# 	else:
# 		print ("您所输入的数小于0")
# else:
# 	print ("您所输入的数大于100")

# s = input("请任意输入一个数：")
# num = int(s)
# if 20 <= num <= 50:
# 	print ("您所输入的数在20~50之间")
# else:
# 	print ("您所输入的数不在20~50之间")

#案例五：
# n = int (input("请输入一个数："))
# if n == 0:
# 	print("您输入的数是0")
# elif n > 0:
# 	print("您输入的数是正数")
# else:
# 	print("您输入的数是负数")

#案例六:
# if 100:
# 	print("真值")
# if bool(100):
# 	print("真值")

#案例七:
# money = int (input("购买的商品总价:"))
# pay = money - 20 if money >= 100 else money
# print ("您需要付款:",pay,"元")




